import json
import requests
from jsonschema import validate

BASE_URL = "https://reqres.in/api"

def test_users_schema():
    response = requests.get(f"{BASE_URL}/users?page=2")
    data = response.json()

    with open("utils/schema_users.json") as f:
        schema = json.load(f)

    validate(instance=data, schema=schema)
