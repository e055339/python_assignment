import pytest
import httpx
import asyncio

# E2E testing requires asyncio with httpx for FastAPI
@pytest.mark.asyncio
async def test_e2e_image_generation():
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        # Step 1: Login
        login_response = await client.post("/login", data={"username": "user1", "password": "password1"})
        assert login_response.status_code == 200
        token = login_response.json()["access_token"]

        # Step 2: Generate image with valid token
        headers = {"Authorization": f"Bearer {token}"}
        image_response = await client.get("/generate_image/?width=100&height=100", headers=headers)
        assert image_response.status_code == 200
        assert image_response.headers["content-type"] == "image/png"
