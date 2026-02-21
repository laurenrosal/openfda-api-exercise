from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = {}
notes = {}
current_id = 1


class User(BaseModel):
    username: str


class Note(BaseModel):
    text: str


# Create account
@app.post("/users", status_code=201)
def create_user(user: User):
    global current_id

    # check duplicate username
    for u in users.values():
        if u["username"] == user.username:
            raise HTTPException(status_code=409, detail="Username already exists")

    users[current_id] = {
        "id": current_id,
        "username": user.username
    }

    notes[current_id] = []
    current_id += 1

    return users[current_id - 1]


# Retrieve account by id
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]


# List all users
@app.get("/users")
def list_users():
    return list(users.values())


# Add text note
@app.post("/users/{user_id}/notes", status_code=201)
def add_note(user_id: int, note: Note):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    notes[user_id].append(note.text)
    return {"notes": notes[user_id]}


# Read text notes
@app.get("/users/{user_id}/notes")
def get_notes(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    return {"notes": notes[user_id]}