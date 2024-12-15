from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Post


def fetch_users(db: Session):
    return db.query(User).all()


def fetch_posts(db: Session):
    return db.query(Post).join(User).all()


def fetch_posts_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()


if __name__ == "__main__":
    db = SessionLocal()

    users = fetch_users(db)
    print("Users:")
    for user in users:
        print(user.username)

    posts = fetch_posts(db)
    print("\nPosts:")
    for post in posts:
        print(f"{post.title} by User ID {post.user_id}")

    user_posts = fetch_posts_by_user(db, user_id=1)
    print("\nPosts by User ID 1:")
    for post in user_posts:
        print(post.title)

    db.close()
