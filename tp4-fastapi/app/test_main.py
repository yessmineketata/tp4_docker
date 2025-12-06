from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item():
    response = client.get("/items/5?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "test"}


def test_secure_endpoint_authorized():
    response = client.get("/secure", headers={"api-key": "mysecretkey"})
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the secure endpoint!"}


def test_secure_endpoint_unauthorized():
    response = client.get("/secure", headers={"api-key": "wrongkey"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}
