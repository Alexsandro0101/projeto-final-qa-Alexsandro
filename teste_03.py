
import requests

def test_usuario_inexistente():
    response = requests.get("https://reqres.in/api/users/999")
    assert response.status_code == 404
