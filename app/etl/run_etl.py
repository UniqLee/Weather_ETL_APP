iimport json
from extract import fetch_weather
from transform import transform
from load import load

def run_etl():
    with open("config/config.json") as f:
        config = json.load(f)

    raw = fetch_weather(config)
    clean = transform(raw)
    load(clean, config["db_path"])
