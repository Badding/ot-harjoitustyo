from db_connection import get_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE users (
            username text,
            password text
        );
    ''')
    connection.commit()


def init_db():
    connection = get_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    init_db()
