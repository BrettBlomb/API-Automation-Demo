import requests

BASE_URL = "https://reqres.in/api"

def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/9999")

    assert response.status_code == 404

import pytest
import requests

BASE_URL = "https://reqres.in/api"

@pytest.mark.parametrize("user_id", [1, 2, 3, 4])
def test_multiple_users(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200

