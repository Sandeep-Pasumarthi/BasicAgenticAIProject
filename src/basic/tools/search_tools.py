from langchain_community.tools.tavily_search import TavilySearchResults

import os


def get_tavily_search():
    return TavilySearchResults(max_results=3)
