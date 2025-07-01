# Multilingual Service

A high-performance RESTful API built with FastAPI to provide multilingual search and data indexing capabilities, powered by Elasticsearch. This service is designed to be run in a containerized environment using Docker.

---

## Features

-   **Fast & Modern API**: Built on **FastAPI** for high performance and automatic interactive API documentation.
-   **Powerful Search**: Leverages **Elasticsearch** for complex, multilingual text search and analysis.
-   **Containerized**: Uses **Docker** and **Docker Compose** for easy setup, deployment, and scalability.
-   **Scalable**: Designed as a microservice that can be easily integrated into a larger system.

---

## Technology Stack

-   **Backend**: Python 3
-   **API Framework**: FastAPI
-   **ASGI Server**: Uvicorn
-   **Database/Search Engine**: Elasticsearch
-   **Containerization**: Docker & Docker Compose

---

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

-   [Python 3.11+](https://www.python.org/downloads/)
-   [Docker](https://www.docker.com/products/docker-desktop/)
-   [Docker Compose](https://docs.docker.com/compose/install/)

---

## Setup and Installation

Follow these steps to get your development environment set up.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd multilingual_service

2. Set Up Backend Services (Elasticsearch)

The project uses Docker Compose to manage the Elasticsearch service.

# This command will start the Elasticsearch container in the background
docker-compose up -d

You can check if the service is running correctly by visiting http://localhost:9200 in your browser or using the command: docker-compose ps.
3. Set Up Python Environment

It is highly recommended to use a virtual environment.

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required Python packages
pip install -r requirements.txt

(Note: If you don't have a requirements.txt file yet, you can create one by running pip freeze > requirements.txt after installing your project's dependencies like fastapi, uvicorn, elasticsearch, etc.)
Running the Application

To run the FastAPI application locally, use the following command from the project's root directory:

uvicorn main:app --host 0.0.0.0 --port 6741 --reload

    main:app: Tells Uvicorn to find the app object in the main.py file.

    --host 0.0.0.0: Makes the server accessible on your network.

    --port 6741: Runs the server on port 6741.

    --reload: Automatically restarts the server whenever you make changes to the code.

Once the server is running, you can access the interactive API documentation at:

    Swagger UI: http://localhost:6741/docs

    ReDoc: http://localhost:6741/redoc

API Endpoints

Below is a brief overview of the main API endpoints. Please refer to the interactive Swagger UI for detailed information on request bodies and responses.
Indexing

    POST /index

        Description: Indexes a new document or a batch of documents into Elasticsearch.

        Request Body: Contains the text content and any associated metadata.

Searching

    GET /search

        Description: Performs a search query against the indexed documents.

        Query Parameters:

            q: The search term.

            lang: The language code (e.g., 'en', 'fa') to specify the search analyzer.

Stopping the Services

To stop all running services (FastAPI and Elasticsearch):

    Press Ctrl+C in the terminal where Uvicorn is running.

    Stop the Docker containers:

    docker-compose down

