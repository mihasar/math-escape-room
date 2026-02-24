import sqlite3
from pathlib import Path

class DBManager:
    
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = Path(__file__).resolve().parent / "escape_room.db"
        self.db_path = str(db_path)

        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS scores(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player TEXT,
                rooms INTEGER,
                mistakes INTEGER
            )
        """)
        conn.commit()
        conn.close()

    def save_score(self, player, rooms, mistakes):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO scores (player, rooms, mistakes) VALUES (?, ?, ?)",
            (player, rooms, mistakes)
        )
        conn.commit()
        conn.close()

    def fetch_scores(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT player, rooms, mistakes FROM scores ORDER BY id DESC")
        rows = cur.fetchall()
        conn.close()
        return rows

    def clear_scores(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("DELETE FROM scores")
        conn.commit()
        conn.close()
        
    