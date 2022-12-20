import pytest
from fastapi.testclient import TestClient
from fastapi import status

from main import app

client = TestClient(app)

data = {
    "name": "Roberlina Prueba",
    "age": 20
}

# def test_create_todo():
#     response = client.post("/todo/", json=data)
#     assert response.status_code == status.HTTP_200_OK
#     res = response.json() 
#     print(res)

def test_home():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"Hello": "World"}

# def test_get_all_todo():
#     response = client.get("/todo", json=data)
#     assert response.status_code == status.HTTP_200_OK
#     assert data in response.json()


# def test_get_todos():
#     response = client.post('/todo/1')
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == {
#         'data': {
#             "id": 1,
#             "name": "Robby",
#             "age": 1
#         }
#     }

# def test_create_todo():
#     response = client.post('/todo', json={"name": "Prueba","age": 21})
#     assert response.status_code == status.HTTP_201_CREATED
#     assert response.json() == {"name": "Prueba","age": 21}