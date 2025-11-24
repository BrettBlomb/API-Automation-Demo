import requests

BASE_URL = "https://reqres.in/api"

def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/9999")

    assert response.status_code == 404
