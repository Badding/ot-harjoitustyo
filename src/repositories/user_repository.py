import db_connection
from werkzeug.security import generate_password_hash, check_password_hash

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
        """Add a new user to the database saving the password hash"""

        password_hash = generate_password_hash(password)
        self._cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?);
        ''', (username, password_hash))

        self._connection.commit()

    def init_new_user_stat(self, user_id):
        """Add a new stat entry for new user to the database"""

        self._cursor.execute('''
            INSERT INTO stats (user_id, top_score, games_played, hands_made) VALUES (?, ?, ?, ?);
        ''', (user_id, 0, 0, '0;0;0;0;0;0;0;0;0;0'))

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

    def get_user_by_id(self, user_id):
        """Get a user from the database by user_id"""

        self._cursor.execute('''
            SELECT * FROM users WHERE rowid = ?;
        ''', (user_id,))
        return self._cursor.fetchone()

    def get_user_stats(self, user_id):
        """Get the stats of a user by user_id"""

        self._cursor.execute('''
            SELECT * FROM stats WHERE user_id = ?;
        ''', (user_id,))
        return self._cursor.fetchone()

    def get_top_scores(self):
        """Get the top scores of all users"""

        self._cursor.execute('''
            SELECT user_id, top_score FROM stats ORDER BY top_score DESC LIMIT 10;
        ''')
        return self._cursor.fetchall()

    def update_top_score(self, user_id, score):
        """Update the top score of a user"""

        self._cursor.execute('''
            UPDATE stats SET top_score = ? WHERE user_id = ?;
        ''', (score, user_id))
        self._connection.commit()

    def update_games_played(self, user_id, games_played):
        """Update the games played of a user"""

        self._cursor.execute('''
            UPDATE stats SET games_played = ? WHERE user_id = ?;
        ''', (games_played, user_id))
        self._connection.commit()

    def update_hands_made(self, user_id, hands_made):
        """Update the hands made of a user"""

        self._cursor.execute('''
            UPDATE stats SET hands_made = ? WHERE user_id = ?;
        ''', (hands_made, user_id))
        self._connection.commit()

    def check_password(self, username, password):
        """Check if the password hash matches the username in the database

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

        return check_password_hash(user['password'], password)


user_repository = UserRepository(db_connection.get_connection())
