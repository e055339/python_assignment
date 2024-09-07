import pytest
from fastapi.testclient import TestClient
from assignment2 import app

client = TestClient(app)

def test_login():
    response = client.post("/login", data={"username": "user1", "password": "password1"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_invalid_login():
    response = client.post("/login", data={"username": "wronguser", "password": "wrongpass"})
    assert response.status_code == 400

def test_logout():
    login_response = client.post("/login", data={"username": "user1", "password": "password1"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/logout", headers=headers)
    assert response.status_code == 200

def test_generate_image():
    login_response = client.post("/login", data={"username": "user1", "password": "password1"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/generate_image/?width=100&height=100", headers=headers)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
