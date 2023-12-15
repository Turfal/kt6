import sqlite3
import os

DB_FILE = "database.db"

def create_database_tables(db_file):
    connection = sqlite3.connect(db_file)
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Client (
                client_id INTEGER PRIMARY KEY,
                full_name TEXT NOT NULL,
                pet_dog_id INTEGER,
                FOREIGN KEY (pet_dog_id) REFERENCES PetDog(dog_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS home (
                kennel_id INTEGER PRIMARY KEY,
                kennel_name TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS PetDog (
                dog_id INTEGER PRIMARY KEY,
                dog_name TEXT NOT NULL,
                kennel_ref_id INTEGER,
                owner_client_id INTEGER,
                FOREIGN KEY (kennel_ref_id) REFERENCES DogKennel(kennel_id),
                FOREIGN KEY (owner_client_id) REFERENCES Client(client_id)
            )
        """)

    print(f"Таблицы в базе данных {db_file} успешно созданы.")

def setup_database(db_file):
    db_exists = os.path.exists(db_file)
    conn = sqlite3.connect(db_file)

    if not db_exists:
        print("База данных не найдена, инициирован процесс её создания.")
        create_database_tables(db_file)
    else:
        print("База данных найдена, подключение успешно.")

    return conn

def main():
    conn = setup_database(DB_FILE)
    conn.close()

if __name__ == "__main__":
    main()
