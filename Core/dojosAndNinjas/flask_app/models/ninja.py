from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = data.get("dojo")

    def __str__(self) -> str:
        return f"Instancia de Ninja {self.name} con ID {self.id}"

    @classmethod
    def get_all(cls):
        resultados_instancias = []
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id"
        resultados = connectToMySQL('dojos_and_ninjas').query_db(query)
        for resultado in resultados:
            
            instancia = cls(resultado)
            datos_dojo = {
                'id': resultado['dojos.id'],
                'name': resultado['dojos.name'],
            }
            instancia_dojo = dojo.Dojo(datos_dojo)
            instancia.dojo = instancia_dojo

            resultados_instancias.append(instancia)

        return resultados_instancias

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )