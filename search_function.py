import json
from serpapi import GoogleSearch
import os


def search_function(lyric: str) -> json:
    params = {
        'engine': "google",
        'q': lyric,
        'location': "United States",
        'api_key': os.getenv("LYRICKEY")
    }
    search_results = GoogleSearch(params)
    print(search_results.get_dict()["organic_results"])
    return search_results.get_dict()
