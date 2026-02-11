import aiosqlite

DB_NAME = "bot.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS pairs (
            pair_id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT UNIQUE,
            user1_id INTEGER,
            user2_id INTEGER
        )
        """)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            pair_id INTEGER,
            role TEXT
        )
        """)
        await db.commit()
