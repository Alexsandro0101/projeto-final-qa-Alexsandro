
import requests

def test_nome_usuario():
    response = requests.get("https://reqres.in/api/users/2")
    json = response.json()
    nome = json['data']['first_name']
    assert nome == "Janet"
