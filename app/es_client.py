
from elasticsearch import Elasticsearch

es_client = Elasticsearch("http://localhost:9200")
INDEX_NAME = "multi_language_documents"

def create_index_if_not_exists():
    """
    Creates the index and its mapping if it does not already exist.
    It uses dynamic_templates to handle undefined language fields.
    """
    if not es_client.indices.exists(index=INDEX_NAME):
        print(f"Creating index '{INDEX_NAME}'...")
        # Define a dynamic mapping.
        # Any new field under the 'body' object will automatically be mapped as 'text'.
        mappings = {
            "properties": {
                "identifier": {"type": "keyword"},
                "body": {
                    "type": "object",
                    "dynamic": True
                }
            },
            "dynamic_templates": [
                {
                    "body_languages": {
                        "path_match": "body.*",  # Matches any field within 'body'
                        "mapping": {
                            "type": "text"      # Maps the field as a text type
                        }
                    }
                }
            ]
        }
        es_client.indices.create(index=INDEX_NAME, mappings=mappings)
        print("Index created successfully.")
    else:
        print(f"Index '{INDEX_NAME}' already exists.")


def insert_document(doc_id: str, document: dict):
    """
    Inserts a document into the index.
    It uses the document's identifier as the _id to prevent duplicates.
    """
    return es_client.index(
        index=INDEX_NAME,
        id=doc_id,
        document=document
    )

def search_documents(query: str | None = None, language: str | None = None, exists_lang: str | None = None):
    """
    Searches for documents based on different criteria.
    - If 'exists_lang' is provided, it finds documents that have a translation in that language.
    - If 'query' is provided, it searches for the query text.
    """
    es_query = None

    if exists_lang:
        # Case 1: Search for documents where the specified language field exists.
        es_query = {
            "exists": {
                "field": f"body.{exists_lang}"
            }
        }
    elif query:
        if language:
            # Case 2: Search for content within a specific language field.
            es_query = {
                "match": {
                    f"body.{language}": query
                }
            }
        else:
            # Case 3: Search for content across all language fields.
            es_query = {
                "multi_match": {
                    "query": query,
                    "fields": ["body.*"]
                }
            }
    else:
        # If no valid search parameters are provided, return an empty list.
        return []

    response = es_client.search(index=INDEX_NAME, query=es_query)
    return [hit["_source"] for hit in response["hits"]["hits"]]