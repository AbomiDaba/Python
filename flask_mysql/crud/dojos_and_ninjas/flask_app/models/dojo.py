from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninja = []

    @classmethod
    def get_all(cls):
        connection = connectToMySQL('dojo_and_ninjas_schema')
        query = 'select * from dojos'
        result = connection.query_db(query)
        dojos = []
        for d in result:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def get_one(cls, data):
        connection = connectToMySQL('dojo_and_ninjas_schema')
        query = 'select * from dojos where id = (id)s'
        result = connection.query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_one_with_ninjas(cls, data):
        connection = connectToMySQL('dojo_and_ninjas_schema')
        query = 'select * from dojos left join ninjas on dojos.id = ninjas.dojos_id where dojos.id = %(id)s'
        result = connection.query_db(query, data)
        print(result)
        dojo = cls(result[0])
        for each_ninja in result:
            if each_ninja == None:
                break
            ninjas_data = {
                'id' : each_ninja['ninjas.id'],
                'first_name' :each_ninja['first_name'],
                'last_name' : each_ninja['last_name'],
                'age': each_ninja['age'],
                'created_at': each_ninja['ninjas.created_at'],
                'updated_at': each_ninja['ninjas.updated_at']
            }
            dojo.ninja.append(ninja.Ninja(ninjas_data))
            print(dojo)
        return dojo

    @classmethod
    def insert(cls, data):
        connection = connectToMySQL('dojo_and_ninjas_schema')
        query = 'insert into dojos (name, created_at, updated_at) values(%(name)s, NOW(), NOW())'
        return connection.query_db(query, data)

    @classmethod
    def update(cls, data):
        connection = connectToMySQL('dojo_and_ninjas_schema')
        query = 'update dojos set name = %(name)s where id = %(id)s'
        return connection.query_db(query, data)

    @classmethod
    def destroy(cls, data):
        connection = connectToMySQL('dojo_and_ninjas_schema')
        query = 'delete from dojos where id = %(id)s'

    

