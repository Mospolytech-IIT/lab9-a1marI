from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User, Post

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD для пользователей
@app.get("/users/")
def read_users(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.post("/users/create/")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    new_user = User(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    return RedirectResponse(url="/users/", status_code=303)

@app.post("/users/delete/{user_id}/")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return RedirectResponse(url="/users/", status_code=303)

@app.get("/users/edit/{user_id}/")
def edit_user(user_id: int, request: Request, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User  not found")
    return templates.TemplateResponse("edit_user.html", {"request": request, "user": user})

@app.post("/users/update/{user_id}/")
def update_user(user_id: int, username: str, email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = username
        user.email = email
        user.password = password
        db.commit()
    return RedirectResponse(url="/users/", status_code=303)

# CRUD для постов
@app.get("/posts/")
def read_posts(request: Request, db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return templates.TemplateResponse("posts.html", {"request": request, "posts": posts})

@app.post("/posts/create/")
def create_post(title: str, content: str, user_id: int, db: Session = Depends(get_db)):
    new_post = Post(title=title, content=content, user_id=user_id)
    db.add(new_post)
    db.commit()
    return RedirectResponse(url="/posts/", status_code=303)

@app.post("/posts/delete/{post_id}/")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
    return RedirectResponse(url="/posts/", status_code=303)

@app.get("/posts/edit/{post_id}/")
def edit_post(post_id: int, request: Request, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return templates.TemplateResponse("edit_post.html", {"request": request, "post": post})

@app.post("/posts/update/{post_id}/")
def update_post(post_id: int, title: str, content: str, user_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.title = title
        post.content = content
        post.user_id = user_id
        db.commit()
    return RedirectResponse(url="/posts/", status_code=303)
