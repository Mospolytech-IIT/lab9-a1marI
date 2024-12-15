from database import Base, engine

# Создание таблиц
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

