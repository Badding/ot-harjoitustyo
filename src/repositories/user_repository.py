import db_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection
        self._cursor = connection.cursor()

    def add_user(self, username, password):
        self._cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?);
        ''', (username, password))
        self._connection.commit()

    def get_user(self, username):
        self._cursor.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))
        return self._cursor.fetchone()

    def get_all_users(self, ):
        self._cursor.execute('''
            SELECT * FROM users;
        ''')
        return self._cursor.fetchall()

    def get_id(self, username):
        self._cursor.execute('''
            SELECT rowid FROM users WHERE username = ?;
        ''', (username,))
        return self._cursor.fetchone()

    def check_password(self, username, password):
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
