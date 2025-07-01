# main.py (Updated with English comments)

from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager

from models import Document
import es_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This function runs when the service starts up.
    print("Starting up...")
    es_client.create_index_if_not_exists()
    yield
    # This section runs when the service shuts down.
    print("Shutting down...")


app = FastAPI(
    title="Multi-language Document Service",
    description="A service to index and search multi-language documents using Elasticsearch.",
    version="1.1.0", # Version updated
    lifespan=lifespan
)

@app.post("/documents", status_code=status.HTTP_201_CREATED)
def add_document(doc: Document):
    """
    Inserts or updates a new multi-language document.
    """
    try:
        response = es_client.insert_document(doc_id=doc.identifier, document=doc.model_dump())
        return {"result": response["result"], "_id": response["_id"]}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.get("/search")
def search(q: str | None = None, lang: str | None = None, exists_lang: str | None = None):
    """
    Searches documents based on content or language availability.

    - **To search for content**: Use the 'q' parameter.
      - Example: `/search?q=hello`
      - To restrict to a specific language, also use 'lang': `/search?q=سلام&lang=fa`

    - **To find documents available in a specific language**: Use the 'exists_lang' parameter.
      - Example: `/search?exists_lang=fa`
    """
    # Check which type of search the user wants to perform.
    if exists_lang:
        # If the user sends conflicting parameters, raise an error.
        if q or lang:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot use 'q' or 'lang' when searching with 'exists_lang'."
            )
        try:
            results = es_client.search_documents(exists_lang=exists_lang)
            return {"results": results}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    elif q:
        # Search by content.
        try:
            results = es_client.search_documents(query=q, language=lang)
            return {"results": results}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    else:
        # If no valid search parameter is provided.
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You must provide either 'q' (for content search) or 'exists_lang' (for language availability)."
        )