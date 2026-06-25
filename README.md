# FastAPI CRUD API

A clean, high-performance REST API demonstrating full CRUD (Create, Read, Update, Delete) operations built with Python and FastAPI. The project manages an in-memory post database with dynamic ID generation and input validation.

Managed efficiently using the **`uv`** fast Python package installer and resolver.

---

##  Features

*   **Create (`POST`)**: Submits new posts using Pydantic schemas for data validation, automatically assigning unique IDs.
*   **Read Individual (`GET`)**: Fetches a single post by its unique ID. Returns explicit `404 Not Found` exceptions if the ID doesn't exist.
*   **Read All (`GET`)**: Retrieves the entire collection of posts from the in-memory database.
*   **Update (`PUT`)**: Updates an existing post's details dynamically while preserving its unique identifier.
*   **Delete (`DELETE`)**: Removes a post seamlessly using lookups via list enumeration.

---

##  Project Structure

```text
supps/
├── main.py            # Main FastAPI application logic & CRUD endpoints
├── pyproject.toml     # Project metadata and dependencies managed by uv
├── uv.lock            # Locked dependency versions for reproducible environments
└── README.md          # Project documentation
