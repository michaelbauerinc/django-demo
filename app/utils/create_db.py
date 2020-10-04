from os import path, system


def create_db_if_not_exists():
    exists = path.exists("/app/db.sqlite3")
    if not exists:
        print("No DB found, creating a new one in /backend/database.")
        system("python manage.py migrate --run-syncdb")
    else:
        print("DB already exists, skipping.")


if __name__ == "__main__":
    create_db_if_not_exists()
