from flask import Flask, render_template, jsonify

import sqlite3
from etl.run_etl import run_etl

app = Flask(__name__)
DB_PATH = "data/weather.db"

def get_latest_weather():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT city,temp, humidity,weather,timestamp FROM  weather ORDER BY timestamp DESC LIMIT 1")
    row= cursor.fetchone()
    conn.close()
    return row

@app.route("/")
def index():
    data = get_latest_weather
    return render_template("index.html",weather=data)

@app.route("/refresh")
def refresh():
    run_etl()
    return "ETL pipeline executed successfully!"

@app.route("/api/weathe")
def api_weather():
    data = get_latest_weather()
    return jsonfy({
        "city":data[0],
        "temp": data[1],
        "humidity":data[2],
        "weather": data[3],
        "timestamp" : data[4]
    })

if __name__ == "__main__":
    app.run(debug=True)