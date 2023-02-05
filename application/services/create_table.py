from application.services.db_connection import DBConnection


def create_table():
    with DBConnection() as connection:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS phone_book(
                phone_id INTEGER NOT NULL PRIMARY kEY UNIQUE,
                contact_name VARCHAR NOT NULL,
                phone_value VARCHAR NOT NULL
                )
                """
            )
