from langchain_core.tools import tool
import re
import requests
from markdownify import markdownify

@tool
def visit_web(url: str) -> str:
    """
    Visit the given URL and extract the main content of the webpage in markdown format.
    Args:
        url (str): The URL of the webpage to visit.
    Returns:
        str: The main content of the webpage converted to markdown.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; LangChainBot/1.0)"
    }
    response = requests.get(url,headers=headers,timeout=20)
    response.raise_for_status()
    markdown_content = markdownify(response.text).strip()
    markdown_content = re.sub(r"\n{3,}","\n\n", markdown_content)
    return markdown_content


@tool
def math(query: str) -> str:
    """
    Evaluate a basic math expression, e.g. 2+2 or 10*5.

    Args:
        query (str): A math expression as a string.

    Returns:
        str: The result of the expression or an error message.
    """
    try:
        result = eval(query,{"__builtins__": None},{})
        return str(result)
    except Exception as e:
        return f"Math error:{str(e)}"

