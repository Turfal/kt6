import os
import pytest
from db import setup_database

DB_FILE = "database.db"

@pytest.fixture(scope='session')
def test_database_created():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    conn = setup_database(DB_FILE)
    assert os.path.exists(DB_FILE)
    conn.close()

def test_database_tables_created():
    conn = setup_database(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert set(tables) == {'Client', 'home', 'PetDog'}

    cursor.execute("PRAGMA table_info(Client);")
    assert cursor.fetchall() == [
        (0, 'client_id', 'INTEGER', 0, None, 1),
        (1, 'full_name', 'TEXT', 0, None, 0),
        (2, 'pet_dog_id', 'INTEGER', 0, None, 0)
    ]

    cursor.execute("PRAGMA table_info(home);")
    assert cursor.fetchall() == [
        (0, 'kennel_id', 'INTEGER', 0, None, 1),
        (1, 'kennel_name', 'TEXT', 0, None, 0)
    ]

    cursor.execute("PRAGMA table_info(PetDog);")
    assert cursor.fetchall() == [
        (0, 'dog_id', 'INTEGER', 0, None, 1),
        (1, 'dog_name', 'TEXT', 0, None, 0),
        (2, 'kennel_ref_id', 'INTEGER', 0, None, 0),
        (3, 'owner_client_id', 'INTEGER', 0, None, 0)
    ]

    conn.close()
