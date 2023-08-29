from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []

    def __str__(self) -> str:
        return f"Instancia de Dojo {self.name} con ID {self.id}"

    @classmethod
    def get_all(cls):
        resultados_instancias = []
        query = "SELECT * FROM dojos"
        resultados = connectToMySQL('dojos_and_ninjas').query_db(query)

        for resultado in resultados:
            instancia = cls(resultado)
            resultados_instancias.append(instancia)

        return resultados_instancias

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )

    @classmethod
    def get(cls, id ):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = { 'id': id }
        resultados = connectToMySQL('dojos_and_ninjas').query_db( query, data )
        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        resultados = connectToMySQL('dojos_and_ninjas').query_db( query, data )
        print("RESULTADOS", resultados)

        instancia_dojo = cls(resultados[0])
        print("INSTANCIA DOJO", instancia_dojo)
        ninjas = []
        for registro in resultados:
            print("REGISTRO", registro)
            data = {
                'id': registro['ninjas.id'],
                'first_name': registro['first_name'],
                'last_name': registro['last_name'], 
                'age': registro['age'],
                'created_at' : registro['created_at'],
                'updated_at' : registro['updated_at'],
                'dojo': instancia_dojo
            }
            instancia_ninjas = Ninja(data)
            ninjas.append(instancia_ninjas)
        
        instancia_dojo.ninjas = ninjas
        return instancia_dojo