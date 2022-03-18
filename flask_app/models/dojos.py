from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.update_at = data["update_at"]
        self.ninjas=[]
    @classmethod
    def muestra_dojo(cls):
        query="SELECT * FROM dojos"
        result= connectToMySQL("esquemas_dojos_y_ninjas").query_db(query)
        dojos=[]
        for d in result:
            dojos.append(cls(d))
        return dojos
    @classmethod
    def agregar(cls, data):
        query = "INSERT INTO dojos (nombre) VALUES (%(nombre)s)"
        results = connectToMySQL("esquemas_dojos_y_ninjas").query_db(query, data)
        dojos = []
        return results
    @classmethod
    def depurar(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("esquemas_dojos_y_ninjas").query_db(query,data)
        dojos = cls(results[0])
        for filtrado in results:
            listafinal = {
                "id": filtrado['ninjas.id'],
                "nombres": filtrado["nombres"],
                "apellido": filtrado["apellido"],
                "edad": filtrado["edad"],
                "created_at": filtrado["ninjas.created_at"],
                "update_at": filtrado["ninjas.update_at"]
            }
            dojos.ninjas.append( Ninja(listafinal) )
        return dojos
