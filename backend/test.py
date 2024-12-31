import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"

search_query = "mars"
tokenizer = "standard"

params = {
            "search_query": search_query,
            "tokenizer": tokenizer,
        }
response = requests.get(f"{BASE_URL}/regular_search/", params=params)


print(response.json())

