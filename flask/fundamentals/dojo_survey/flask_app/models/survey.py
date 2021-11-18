from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at= data['updated_at']

    @classmethod
    def get_last(cls):
        connection = connectToMySQL('dojo_survey')
        query = 'select * from surveys order by surveys.id desc limit 1;'
        result = connection.query_db(query)
        return cls(result[0])
    @classmethod
    def create(cls, data):
        connection = connectToMySQL('dojo_survey')
        query = 'insert into surveys (name, location, language, comments) value(%(name)s, %(location)s, %(language)s, %(comments)s )'
        return connection.query_db(query, data)

    @staticmethod
    def validate_survey(data):
        is_valid = True
        if len(data['name']) < 3:
            flash('Name must be at least 3 characters')
            is_valid = False
        if len(data['location']) < 3:
            flash('Must choose a dojo location')
            is_valid = False
        if len(data['language']) < 3:
            flash('Must choose a dojo language')
            is_valid = False
        if len(data['comments']) < 3:
            flash('Comments must be at least 3 characters')
            is_valid = False
        return is_valid
