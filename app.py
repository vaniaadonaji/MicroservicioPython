from flask import Flask
from pymongo import MongoClient

from computadora_controller import ComputadoraController

class App:
    def __init__(self):
        self.app = Flask(__name__)

        # Cadena de conexión de MongoDB Atlas
        self.app.config["MONGO_URI"] = "mongodb+srv://vaniadonajitorres:02Mayovd@cluster0.ddgjd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        
        # Crear cliente MongoDB
        self.client = MongoClient(self.app.config["MONGO_URI"])
        self.db = self.client.get_database('computadoras_db')

        # Verificar conexión
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(f"Error de conexión: {e}")
        
        # Aquí puedes continuar con la configuración de rutas, controladores, etc.
        self.computadora_controller = ComputadoraController(self.db)
        self.register_routes()

    def register_routes(self):
        # Aquí se registran las rutas para las computadoras
        self.app.add_url_rule('/computadoras', view_func=self.computadora_controller.obtener_computadoras, methods=["GET"])
        self.app.add_url_rule('/computadoras/<id>', view_func=self.computadora_controller.obtener_computadora, methods=["GET"])
        self.app.add_url_rule('/computadoras', view_func=self.computadora_controller.agregar_computadora, methods=["POST"])
        self.app.add_url_rule('/computadoras/<id>', view_func=self.computadora_controller.editar_computadora, methods=["PUT"])
        self.app.add_url_rule('/computadoras/<id>', view_func=self.computadora_controller.eliminar_computadora, methods=["DELETE"])

    def run(self):
        self.app.run(debug=True)
    


if __name__ == '__main__':
    app = App()
    app.run()
