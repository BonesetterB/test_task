from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connect_to_database():
    db_url = 'sqlite:///db.sqlite3'
    engine = create_engine(db_url)
    
    try:
        Session = sessionmaker(bind=engine)
        session = Session()

        return session

    except Exception as e:
        print(f"Помилка підключення до бази даних: {e}")
        return None

if __name__ == "__main__":

    session = connect_to_database()

    if session:
        print("Підключено до бази даних SQLite!")
    else:
        print("Не вдалося підключитися до бази даних SQLite.")
