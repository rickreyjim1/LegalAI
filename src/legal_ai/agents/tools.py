"""Web and RAG search tools for finding academic and local papers"""

import requests
from crewai.tools import tool
from .rag_system import RAGSystem

@tool("Web Search Tool")
def web_search_tool(query: str) -> str:
    """
    Search the web for recent academic papers and credible sources.
    Returns formatted results with titles, authors, and publication info.
    Uses CrossRef API for academic paper search.
    """
    try:
        search_url = f"https://api.crossref.org/works?query={query}&rows=5"
        response = requests.get(search_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            results = []
            
            for idx, item in enumerate(data.get('message', {}).get('items', [])[:5], 1):
                title = item.get('title', ['Unknown'])[0] if item.get('title') else 'Unknown'
                authors = []
                for author in item.get('author', [])[:3]:
                    given = author.get('given', '')
                    family = author.get('family', '')
                    if given and family:
                        authors.append(f"{given[0]}. {family}")
                
                authors_str = ', '.join(authors) if authors else 'Unknown Authors'
                journal = item.get('container-title', ['Unknown Journal'])[0] if item.get('container-title') else 'Unknown Journal'
                year = item.get('published', {}).get('date-parts', [[0]])[0][0] if item.get('published') else 'N/A'
                doi = item.get('DOI', 'N/A')
                
                results.append(f"{idx}. {authors_str}, \"{title}\", {journal}, {year}. DOI: {doi}")
            
            return "\n".join(results) if results else "No results found"
        else:
            return "Web search unavailable. Using general knowledge for references."
    
    except Exception as e:
        return f"Web search unavailable: {str(e)}. Using general knowledge for references."

@tool("Local PDF Search Tool")
def rag_search_tool(query: str) -> str:
    """
    Search local PDF documents in the pdf_library folder for context.
    Use this tool to find information from textbooks, laws, and internal documents.
    """
    try:
        rag = RAGSystem(pdf_folder="original_documents/pdf_library", db_folder="original_documents/rag_db")
        results = rag.search(query, top_k=5)
        if not results:
            return "No relevant local documents found in the PDF library."
        return rag.format_results_for_citation(results, 'IEEE')
    except Exception as e:
        return f"RAG search failed: {str(e)}"

@tool("Image Generation Tool")
def image_generation_tool(prompt_and_filename: str) -> str:
    """
    Generates an AI image based on a prompt and saves it locally.
    Input must be exactly in this format: "Prompt text here|filename.png"
    Example: "A futuristic cyborg lawyer in a courtroom|cyborg_lawyer.png"
    """
    import urllib.parse
    import os
    
    try:
        parts = prompt_and_filename.split('|')
        if len(parts) != 2:
            return "Error: Input must be exactly 'prompt|filename.png'"
            
        prompt = parts[0].strip()
        filename = parts[1].strip()
        
        # Ensure filename ends with .png
        if not filename.endswith('.png'):
            filename += '.png'
            
        # URL encode the prompt
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=768&nologo=true"
        
        # Ensure Images directory exists
        os.makedirs("Images", exist_ok=True)
        filepath = os.path.join("Images", filename)
        
        # Download the image
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return f"Successfully generated and saved image to {filepath}"
        else:
            return f"Failed to generate image. API returned {response.status_code}"
            
    except Exception as e:
        return f"Image generation failed: {str(e)}"
