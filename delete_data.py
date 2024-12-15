from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Post


def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()


def delete_user_and_posts(db: Session, user_id: int):
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    for post in posts:
        db.delete(post)
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()


if __name__ == "__main__":
    db = SessionLocal()

    delete_post(db, post_id=2)
    delete_user_and_posts(db, user_id=2)

    db.close()
    print("Данные удалены!")
