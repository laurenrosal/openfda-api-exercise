from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

# In-memory storage
users: Dict[int, dict] = {}
notes: Dict[int, List[str]] = {}
current_id = 1


class UserCreate(BaseModel):
    username: str


class NoteCreate(BaseModel):
    text: str


#Create account
@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    global current_id

    # Check if username already exists
    for u in users.values():
        if u["username"] == user.username:
            raise HTTPException(status_code=409, detail="Username already exists")

    new_user = {
        "id": current_id,
        "username": user.username
    }

    users[current_id] = new_user
    notes[current_id] = []
    current_id += 1

    return new_user


#Retrieve account by id
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    return users[user_id]


#List all users
@app.get("/users")
def list_users():
    return list(users.values())


#Add text note
@app.post("/users/{user_id}/notes", status_code=201)
def add_note(user_id: int, note: NoteCreate):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    notes[user_id].append(note.text)
    return {"message": "Note added", "notes": notes[user_id]}


#Read text notes
@app.get("/users/{user_id}/notes")
def get_notes(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    return {"notes": notes[user_id]}
