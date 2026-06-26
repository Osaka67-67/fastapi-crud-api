<div align="center">
  <img width="220" height="220" alt="i-did-it-anime" src="https://github.com/user-attachments/assets/6877963c-66fa-4b45-a2c5-93fc37908289" />
</div>

# FastAPI CRUD API (PostgreSQL Edition)

<img src="https://media.tenor.com/E1v8U0I0X5IAAAAC/i-did-it-anime.gif" width="300" alt="I Did It! Anime Celebration">

A clean, high-performance REST API demonstrating full CRUD (Create, Read, Update, Delete) operations built with Python and FastAPI. This project connects to a **PostgreSQL database** using native SQL queries via **`psycopg`**. 

This repository reflects a learning phase moving away from raw in-memory storage, with future plans to transition to an Object-Relational Mapper (ORM) like **SQLAlchemy**.

Managed efficiently using the **`uv`** fast Python package installer and resolver.

---

##  Features

<div align="center">
  <img width="300" height="250" alt="chika-love-is-war" src="https://github.com/user-attachments/assets/817119e3-623b-4c9a-900c-7f05ee490720" />
</div>

* **Database-Backed (PostgreSQL)**: Migrated from local dict arrays to persistent relational storage.
* **Resilient Connection Loop**: Implements an automatic retry mechanism with `time.sleep` to wait out database connection lags or boot issues.
* **Environment Isolation**: Securely reads sensitive database credentials using `.env` configurations via `python-dotenv`.
* **Structured Data Validation**: Uses Pydantic to strictly type-check payload inputs before sending data down to the database layers.
* **Full CRUD Operations**:
  * **Create (`POST`)**: Inserts new posts into PostgreSQL and returns the freshly generated record.
  * **Read Individual (`GET`)**: Fetches a single post by its ID, issuing a precise `404 Not Found` if it is missing.
  * **Read All (`GET`)**: Extracts all entries smoothly using cursor dictionary row formatting.
  * **Update (`PUT`)**: Updates table data dynamically.
  * **Delete (`DELETE`)**: Safely removes records using table matching clauses and returns the deleted record as confirmation.

---

##  Project Structure

```text
supps/
├── .env               # Environment variables for secure DB credentials (Keep Git-ignored!)
├── main.py            # Main FastAPI application logic, raw SQL integration, & endpoints
├── pyproject.toml     # Project metadata and dependencies managed by uv
├── uv.lock            # Locked dependency versions for reproducible environments
└── README.md          # Project documentation
```

---

##  Setup & Configuration



### 1. Environment Variables
Create a `.env` file inside the root of your `supps/` directory and populate your PostgreSQL parameters:

user=your_postgres_user
password=your_postgres_password
dbname=your_database_name
host=localhost

### 2. Run the Application
Use `uv` to execute or launch your FastAPI live development environment:

uv run uvicorn main:app --reload

---

Arigatou for witnessing this hehe :) 

<div align="center">
  <img width="374" height="374" alt="umi-katou" src="https://github.com/user-attachments/assets/d0795fc0-9943-4fcd-8c48-027d42fcfad6" />
</div>

---
