from user_app.config.mysql_connection import connect_to_mysql

DATABASE = "user_practice"


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, form_data):
        query = """
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s);
"""
        user_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return user_id

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM users
        """
        results = connect_to_mysql(DATABASE).query_db(query)
        users = []
        for dictionary in results:
            users.append(User(dictionary))
        return users

    @classmethod
    def get_one(cls, user_id):
        query = """
            SELECT * FROM users
            WHERE id = %(user_id)s
"""
        data = {"user_id": user_id}
        result = connect_to_mysql(DATABASE).query_db(query, data)
        user = User(result[0])
        return user

    @classmethod
    def update(cls, form_data):
        pass

    @classmethod
    def delete(cls, user_id):
        pass
