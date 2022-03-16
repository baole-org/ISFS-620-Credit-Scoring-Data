from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import User, Role, Gender

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("35c63a63-16da-4af9-af73-b5a8b3f3aa5f"),
        # id = uuid4(),
        first_name='Mark',
        last_name = 'Le',
        gender = Gender.male,
        roles = [Role.admin]
        ),
    User(
        id=UUID("ed0c6fe3-fd43-4f62-abab-ab88f00704d1"),
        # id = uuid4(),
        first_name='Alex',
        last_name = 'Jones',
        gender = Gender.female,
        roles = [Role.student, Role.user]
        )
]

@app.get("/")
async def root():
    return {"hello": "world"}

@app.get('/api/v1/users')
async def fetch_user():
    return db

@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'user with id: {user_id} does not exist'
    )

