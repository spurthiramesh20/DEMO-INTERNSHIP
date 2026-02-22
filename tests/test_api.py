import requests
from app.main import fetch_data

def test_fetch_data_returns_response():
    api_url = "https://official-joke-api.appspot.com/jokes/programming/random"
    data = fetch_data(api_url)

    assert data is not None