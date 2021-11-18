from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        connection = connectToMySQL('user_schema')
        query = 'select * from users'
        results = connection.query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        connection = connectToMySQL('user_schema')
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connection.query_db( query, data )

    @classmethod
    def get_one(cls, data):
        connection = connectToMySQL('user_schema')
        query = 'select * from users where id = %(id)s'
        result = connection.query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        connection = connectToMySQL('user_schema')
        query = 'update users set first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s where id = %(id)s'
        return connection.query_db(query,data)

    @classmethod
    def destroy(cls, data):
        connection = connectToMySQL('user_schema')
        query = 'delete from users where id = %(id)s'
        return connection.query_db(query, data)