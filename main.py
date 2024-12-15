from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Post, Base

app = FastAPI()

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)

@app.post("/users/")
def create_user(username: str, email: str, password: str):
    session = Session()
    new_user = User(username=username, email=email, password=password)
    session.add(new_user)
    session.commit()
    session.close()
    return {"message": "User  created"}

@app.get("/users/")
def read_users():
    session = Session()
    users = session.query(User).all()
    session.close()
    return users

@app.post("/posts/")
def create_post(title: str, content: str, user_id: int):
    session = Session()
    new_post = Post(title=title, content=content, user_id=user_id)
    session.add(new_post)
    session.commit()
    session.close()
    return {"message": "Post created"}

@app.get("/posts/")
def read_posts():
    session = Session()
    posts = session.query(Post).all()
    session.close()
    return posts

# Запуск приложения производится через команду: uvicorn main:app --reload

