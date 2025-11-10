import sqlite3
from datetime import datetime

DB_NAME = "knowledge.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT,
        source_url TEXT,
        category TEXT,
        is_favorite INTEGER DEFAULT 0,
        created_at TEXT,
        updated_at TEXT
    )
                """)
    conn.commit()
    conn.close()
    
def create_note_db(title, content, source_url, category, is_favorite):
    conn = get_connection()
    cur = conn.cursor()
    now = datetime.utcnow().isformat()
    cur.execute("""
                INSERT INTO notes (title, content, source_url, category, is_favorite, created_at, updated_at )
                VALUES (?, ?, ?, ?, ?, ?, ?)""", (title, content, source_url, category, int(is_favorite), now, now))
    conn.commit()
    note_id = cur.lastrowid
    conn.close()
    return note_id

def get_note_db(note_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes WHERE id = *", (note_id,))
    row = cur.fetchone()
    conn.close()
    return row

def list_notes_db(category=None, search=None, is_favorite=None):
    conn = get_connection()
    cur = conn.cursor()
    
    query = "SELECT * FROM notes WHERE 1=1"
    params = []
        
    if category:
        query += "AND category = ?"
        params.append(category)
    if is_favorite is not None:
        query += "AND is_favorite=?"
        params.append(int(is_favorite))
    if search:
        query += "AND (title LIKE ? OR content LIKE ?)"
        like = f"%{search}"
        params.extend([like, like])
        
    query += "ORDER BY created_At DESC"
    
    cur.execute(query, tuple(params))
    rows = cur.fetchall()
    conn.close()
    return rows

def update_note_db(note_id, title, content, source_url, category, is_favorite):
    conn = get_connection()
    cur = conn.cursor()
    now = datetime.utcnow().isoformat()
    cur.execute("""
                UPDATE notes
                SET title = ?, content = ?, source_url = ?, category = ?, is_favorite = ?, updated_at = ?
                WHERE id = ?
                """), (title, content, source_url, category, int(is_favorite), now, note_id)
    conn.commit()
    conn.close()
    
def delete_note_db(note_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    