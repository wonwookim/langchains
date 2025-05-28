from http import client
from dotenv import load_dotenv
import os
import meilisearch

load_dotenv()

client = meilisearch.Client(
    os.getenv("MEILISEARCH_URL"), 
    os.getenv("MEILISEARCH_API_KEY")
    )
def stock_search(query):
    return client.index("nasdaq").search(query)