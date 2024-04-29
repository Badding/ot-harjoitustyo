import db_connection


class UserRepository:
    """User repository class. Handles all user related database operations"""

    def __init__(self, connection):
        """Constructor for the UserRepository class

        Args:
            connection (sqlite3.Connection):
                The connection to the database
        """

        self._connection = connection
        self._cursor = connection.cursor()

    def add_user(self, username, password):
        """Add a new user to the database"""

        self._cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?);
        ''', (username, password))
        self._connection.commit()

    def get_user(self, username):
        """Get a user from the database by username"""

        self._cursor.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))
        return self._cursor.fetchone()

    def get_all_users(self, ):
        """Get all users from the database"""

        self._cursor.execute('''
            SELECT * FROM users;
        ''')
        return self._cursor.fetchall()

    def get_id(self, username):
        """Get the id of a user by username"""

        self._cursor.execute('''
            SELECT rowid FROM users WHERE username = ?;
        ''', (username,))
        return self._cursor.fetchone()

    def check_password(self, username, password):
        """Check if the password matches the username

        Args:
            username (str):
                The username to check
            password (str):
                The password to check
        Returns:
            bool: True if the password matches the username
        """

        user = self.get_user(username)
        if user is None:
            return False
        return user['password'] == password


user_repository = UserRepository(db_connection.get_connection())

"""
if __name__ == '__main__':
    connection = db_connection.get_connection()

    init_db()

    cursor = connection.cursor()

    #connection.close()
"""
