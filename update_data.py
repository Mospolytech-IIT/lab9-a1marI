from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Post

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Обновление email пользователя
def update_user_email(username, new_email):
    user = session.query(User).filter_by(username=username).first()
    if user:
        user.email = new_email
        session.commit()

# Обновление поста
def update_post_content(post_id, new_content):
    post = session.query(Post).filter_by(id=post_id).first()
    if post:
        post.content = new_content
        session.commit()

if __name__ == "__main__":
    update_user_email('user1', 'new_email@example.com')
    update_post_content(1, 'Updated content for Post 1')
