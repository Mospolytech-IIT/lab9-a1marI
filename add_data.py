from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Post

def add_users(db: Session):
    users = [
        User(username="user1", email="user1@example.com", password="password1"),
        User(username="user2", email="user2@example.com", password="password2"),
    ]
    db.add_all(users)
    db.commit()

def add_posts(db: Session):
    posts = [
        Post(title="Post 1", content="Content of post 1", user_id=1),
        Post(title="Post 2", content="Content of post 2", user_id=2),
    ]
    db.add_all(posts)
    db.commit()

if __name__ == "__main__":
    db = SessionLocal()
    add_users(db)
    add_posts(db)
    db.close()
    print("Данные добавлены!")
