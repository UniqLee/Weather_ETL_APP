import sqlite3

def load(data, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temp REAL,
            humidity INTEGER,
            weather TEXT,
            timestamp INTEGER
        )
    ''')
    cursor.execute('''
        INSERT INTO weather (city, temp, humidity, weather, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (data["city"], data["temp"], data["humidity"], data["weather"], data["timestamp"]))
    conn.commit()
    conn.close()
