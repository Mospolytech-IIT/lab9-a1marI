from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Post

engine = create_engine('sqlite:///database.db')  # Для SQLite
Session = sessionmaker(bind=engine)
session = Session()


# Добавление пользователей
def add_users():
    user1 = User(username='user1', email='user1@example.com', password='password1')
    user2 = User(username='user2', email='user2@example.com', password='password2')
    session.add(user1)
    session.add(user2)
    session.commit()


# Добавление постов
def add_posts():
    user1 = session.query(User).filter_by(username='user1').first()
    user2 = session.query(User).filter_by(username='user2').first()

    post1 = Post(title='Post 1', content='Content of Post 1', user_id=user1.id)
    post2 = Post(title='Post 2', content='Content of Post 2', user_id=user2.id)

    session.add(post1)
    session.add(post2)
    session.commit()


if __name__ == "__main__":
    add_users()
    add_posts()
