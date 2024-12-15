from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Post


def update_user_email(db: Session, user_id: int, new_email: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()


def update_post_content(db: Session, post_id: int, new_content: str):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.content = new_content
        db.commit()


if __name__ == "__main__":
    db = SessionLocal()

    update_user_email(db, user_id=1, new_email="new_user1@example.com")
    update_post_content(db, post_id=1, new_content="Updated content of post 1")

    db.close()
    print("Данные обновлены!")
