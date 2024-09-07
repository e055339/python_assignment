from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()


fake_users_db = {
    "user1": {"username": "user1", "password": "password1"},
}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


sessions = {}



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
