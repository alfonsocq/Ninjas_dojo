from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self,data):
        self.id = data["id"]
        self.nombres = data["nombres"]
        self.apellido = data["apellido"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.update_at = data["update_at"]
        
    @classmethod
    def mostrar_usuarios(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL("esquemas_dojos_y_ninjas").query_db(query)
        ninjas = []
        for u in results:
            ninjas.append(cls(u))
        return ninjas
        
    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO ninjas (nombres, apellido, edad, dojo_id) VALUES (%(nombres)s, %(apellido)s, %(edad)s, %(dojo_id)s)"
        results = connectToMySQL("esquemas_dojos_y_ninjas").query_db(query, data)
        ninjas = []
        return results

   