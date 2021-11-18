from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls, data):
        connection = connectToMySQL('dojo_and_ninjas_schema')
        query = 'select * from ninjas where id = (id)s'
        result = connection.query_db(query, data)
        return cls(result)

    @classmethod
    def insert(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name,age,dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojo_and_ninjas_schema').query_db(query,data)

    @classmethod
    def update(cls, data):
        connection = connectToMySQL('dojo_and_ninjas_schema')
        query = 'update ninjas set first_name = %(first_name)s, last_name = %(last_name)s, %(age)s  where id = %(id)s'
        return connection.query_db(query, data)

    @classmethod
    def destroy(cls, data):
        connection = connectToMySQL('dojo_and_ninjas_schema')
        query = 'delete from ninjas where id = %(id)s'
        return connection.query_db(query, data)