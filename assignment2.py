import os
from fastapi import FastAPI, HTTPException, Depends, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from PIL import Image
from io import BytesIO
import time
from dotenv import load_dotenv
import google.cloud.logging
import logging

load_dotenv()

google_credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
logging_client = google.cloud.logging.Client.from_service_account_json(google_credentials_path)
logging_client.setup_logging()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI()

fake_users_db = {
    "user1": {"username": "user1", "password": "password1"},
}

sessions = {}
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if user and user["password"] == password:
        return username
    return None


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = f"token-{username}"
    sessions[token] = username
    return {"access_token": token, "token_type": "bearer"}


@app.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    if token not in sessions:
        raise HTTPException(status_code=401, detail="Invalid token")

    del sessions[token]
    return {"message": "Logged out successfully"}


@app.get("/generate_image/")
def generate_image(width: int, height: int, token: str = Depends(oauth2_scheme)):
    start_time = time.time()

    if token not in sessions:
        raise HTTPException(status_code=401, detail="Invalid token")

    logger.info(f"User {sessions[token]} requested an image of size {width}x{height}")

    img = Image.new('RGB', (width, height), color='blue')

    img_buffer = BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    if time.time() - start_time > 0.7:
        raise HTTPException(status_code=504, detail="Processing time exceeded 0.7 seconds")

    return Response(img_buffer.getvalue(), media_type="image/png")

