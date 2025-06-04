import requests

def test_services_talk():
    r = requests.get("http://localhost:5002/trigger")
    assert "Hello from B" in r.text