import requests

def fetch_weather(config):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={config['city']}&units={config['units']}&appid={config['api_key']}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
