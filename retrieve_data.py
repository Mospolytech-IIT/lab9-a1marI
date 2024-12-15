from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Post

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Извлечение всех пользователей
def get_all_users():
    users = session.query(User).all()
    for user in users:
        print(user.username, user.email)

# Извлечение всех постов с пользователями
def get_all_posts():
    posts = session.query(Post).join(User).all()
    for post in posts:
        print(post.title, post.author.username)

# Извлечение постов конкретного пользователя
def get_posts_by_user(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        posts = user.posts
        for post in posts:
            print(post.title)

if __name__ == "__main__":
    get_all_users()
    get_all_posts()
    get_posts_by_user('user1')
