
import requests

def test_status_code():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
