import requests

BASE_URL = "https://reqres.in/api"

def test_get_users_success():
    response = requests.get(f"{BASE_URL}/users?page=2")
    data = response.json()

    assert response.status_code == 200
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
    assert "email" in data["data"][0]
