from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Post

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Удаление поста
def delete_post(post_id):
    post = session.query(Post).filter_by(id=post_id).first()
    if post:
        session.delete(post)
        session.commit()

# Удаление пользователя и его постов
def delete_user(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        session.delete(user)
        session.commit()

if __name__ == "__main__":
    delete_post(1)
    delete_user('user2')
