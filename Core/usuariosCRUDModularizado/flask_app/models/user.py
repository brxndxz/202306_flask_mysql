from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_db').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
            print(user)
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(em)s , NOW() , NOW() );"
        return connectToMySQL('users_db').query_db( query, data )
    
    @classmethod
    def get(cls, id ):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id': id}
        results = connectToMySQL('users_db').query_db(query, data)
        if results:
            return cls(results[0])
        return None
    
    def delete(self):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {'id': self.id}
        connectToMySQL('users_db').query_db(query, data)
        return True
    
    def update(self):
        query = "UPDATE users SET first_name = %(fname)s, last_name =  %(lname)s, email =  %(em)s, updated_at = NOW() WHERE id = %(id)s"
        data = {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'em': self.em
        }
        connectToMySQL('users_db').query_db( query, data )
        return True
