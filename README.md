**Personal Knowledge API**

A simple RESTful API built with *FastAPI* and *SQLite* to manage personal notes or knowledge entries.
Users can *create*, *read*, *update*, and *delete* notes with optional *filtering* and *search* functionality.

------------------------------------------------------------

**Features**
- Add, edit, delete, and list notes
- Filter notes by *category*, *favorite status*, or *keywords*
- *SQLite* database integration
- Automatic *FastAPI documentation* available at /docs

------------------------------------------------------------

**Tech Stack**
- *Python 3.9+*
- *FastAPI*
- *SQLite*
- *Uvicorn*

------------------------------------------------------------

**Installation**

1. Clone the repository:
   git clone https://github.com/yourusername/personal-knowledge-api.git
   cd personal-knowledge-api

2. Create and activate a virtual environment:
   python -m venv .venv
   .venv\Scripts\activate   (On Windows)
   source .venv/bin/activate   (On macOS/Linux)

3. Install dependencies:
   pip install fastapi uvicorn

4. Run the API:
   uvicorn main:app --reload

5. Open the browser:
   http://127.0.0.1:8000/docs

------------------------------------------------------------

*Example JSON Body*
{
  "title": "FastAPI with SQLite",
  "content": "Learning how to build REST APIs using FastAPI and SQLite.",
  "source_url": "https://fastapi.tiangolo.com/",
  "category": "Backend",
  "is_favorite": true
}
