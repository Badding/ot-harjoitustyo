from db_connection import get_connection


def drop_tables(connection):
    """Drop tables if they exist

    Args:
        connection: Connection to the database
    """

    cursor = connection.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')
    cursor.execute('''
        DROP TABLE IF EXISTS stats;
    ''')
    connection.commit()


def create_tables(connection):
    """Create tables

    Args:
        connection: Connection to the database
    """
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE users (
            id integer primary key autoincrement,
            username text,
            password text
        );
    ''')
    cursor.execute('''
        CREATE TABLE stats (
            id integer primary key autoincrement,
            user_id integer,
            game_mode integer,
            top_score integer,
            games_played integer,
            hands_made text,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
    ''')
    connection.commit()


def init_db():
    """Initialize the database"""
    connection = get_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    init_db()
