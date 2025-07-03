# Multilingual Search Service with Elasticsearch and FastAPI

This project provides a high-performance RESTful API for indexing and searching multilingual documents using Elasticsearch as the backend. The service is built with Python and FastAPI and is fully containerized using Docker for easy setup and deployment.

The key feature is its ability to handle documents with text in various languages dynamically, without needing to pre-define the languages in the schema.

---

## Features
- **Fast & Modern API**: Built on FastAPI for high performance and automatic interactive API documentation.
- **Powerful Search**: Leverages Elasticsearch for complex, multilingual text search and analysis.
- **Containerized**: Uses Docker and Docker Compose for easy setup, deployment, and scalability.
- **Scalable**: Designed as a microservice that can be easily integrated into a larger system.

---

## Technology Stack
- **Backend**: Python 3.9
- **API Framework**: FastAPI
- **ASGI Server**: Uvicorn
- **Database/Search Engine**: Elasticsearch
- **Containerization**: Docker & Docker Compose

---

## Prerequisites
Before you begin, ensure you have the following installed on your local machine:
- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Project Structure
```
Multilingual-Service/
├── app/
│   ├── es_client.py
│   ├── main.py
│   └── models.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd Multilingual-Service
```

### 2. Run with Docker Compose (Recommended)
This will start both Elasticsearch and the FastAPI API.
```bash
docker-compose up --build
```
- **FastAPI** will be available at: [http://localhost:4321/docs](http://localhost:4321/docs)
- **Elasticsearch** will be available at: [http://localhost:1234](http://localhost:1234)

To stop all running services:
```bash
docker-compose down
```

### 3. Run Locally (Without Docker)
> **Note:** You must have a local Elasticsearch instance running on `localhost:9200` for this to work.


## API Endpoints

### 1. Index a Document
This endpoint adds a new document to the search index or updates an existing one with the same identifier.
- **URL:** `/documents`
- **Method:** POST
- **Body:** JSON object with the document's identifier and a body object containing language-to-text mappings.

**Example using curl:**
```bash
curl -X POST "http://localhost:4321/documents" \
     -H "Content-Type: application/json" \
     -d '{
           "identifier": "doc-001",
           "body": {
             "en": "Hello world! This is a test of the search service.",
             "fa": "سلام دنیا! این یک آزمایش برای سرویس جستجو است.",
             "es": "Hola mundo! Esta es una prueba del servicio de búsqueda."
           }
         }'
```

### 2. Search for Documents
This endpoint searches for documents containing a specific query within the text of a specified language, or finds documents available in a specific language.
- **URL:** `/search`
- **Method:** GET
- **Query Parameters:**
    - `q` (optional): The search term.
    - `lang` (optional): The 2-letter language code to search within (e.g., en, fa).
    - `exists_lang` (optional): Find documents available in a specific language.

**Examples using curl:**

Search for "test" in English documents:
```bash
curl --get "http://localhost:4321/search" --data-urlencode "q=test" --data-urlencode "lang=en"
```

Search for "آزمایش" in Persian (Farsi) documents:
```bash
curl --get "http://localhost:4321/search" --data-urlencode "q=آزمایش" --data-urlencode "lang=fa"
```

Find all documents that have a Persian translation:
```bash
curl --get "http://localhost:4321/search" --data-urlencode "exists_lang=fa"
```

---

## Stopping the Services
To stop all running services (FastAPI and Elasticsearch):
```bash
docker-compose down
```

---

## Notes
- The API is documented with Swagger UI at `/docs` and ReDoc at `/redoc`.
- Make sure the ports in `docker-compose.yml` match those in your documentation and code.
- For production, consider using environment variables for configuration.