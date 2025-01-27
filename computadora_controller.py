from flask import jsonify, request
from bson.objectid import ObjectId

class ComputadoraController:
    def __init__(self, db):
        self.db = db

    def agregar_computadora(self):
        data = request.get_json()
        
        required_fields = ['marca', 'modelo', 'procesador', 'ram', 'almacenamiento', 'precio']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Faltan datos necesarios"}), 400
        
        computadora = {
            "marca": data["marca"],
            "modelo": data["modelo"],
            "procesador": data["procesador"],
            "ram": data["ram"],
            "almacenamiento": data["almacenamiento"],
            "precio": data["precio"],
            "tarjeta_grafica": data.get("tarjeta_grafica", ""),
            "pantalla": data.get("pantalla", ""),
            "peso": data.get("peso", ""),
            "anio_lanzamiento": data.get("anio_lanzamiento", ""),
            "color": data.get("color", ""),
            "sistema_operativo": data.get("sistema_operativo", ""),
            "conectividad": {
                "wifi": data.get("wifi", ""),
                "bluetooth": data.get("bluetooth", ""),
                "ethernet": data.get("ethernet", "")
            },
            "puertos": {
                "usb": data.get("usb", ""),
                "hdmi": data.get("hdmi", ""),
                "audio": data.get("audio", "")
            },
            "bateria": data.get("bateria", ""),
            "duracion_bateria": data.get("duracion_bateria", ""),
            "tipo_pantalla": data.get("tipo_pantalla", ""),
            "resolucion": data.get("resolucion", ""),
            "teclado": {
                "retroiluminado": data.get("retroiluminado", False),
                "idioma": data.get("idioma_teclado", "")
            },
            "webcam": data.get("webcam", ""),
            "audio": data.get("audio", ""),
            "seguridad": {
                "lector_huellas": data.get("lector_huellas", False),
                "reconocimiento_facial": data.get("reconocimiento_facial", False),
                "tpm": data.get("tpm", False)
            },
            "expansion": {
                "slots_ram": data.get("slots_ram", 0),
                "puertos_almacenamiento": data.get("puertos_almacenamiento", 0)
            },
            "garantia": data.get("garantia", ""),
            "precio_venta": data.get("precio_venta", data["precio"]),
            "accesorios_incluidos": data.get("accesorios_incluidos", ""),
            "recomendado_para": data.get("recomendado_para", ""),
            "opiniones_usuarios": data.get("opiniones_usuarios", ""),
            "condicion": data.get("condicion", "Nuevo"),
            "fabricante_tarjeta_grafica": data.get("fabricante_tarjeta_grafica", ""),
        }
        
        result = self.db.computadoras.insert_one(computadora)
        computadora["_id"] = str(result.inserted_id)  # Convertimos ObjectId a string
        
        return jsonify(computadora), 201

    def obtener_computadoras(self):
        # Asegúrate de que 'computadoras' sea el nombre correcto de tu colección
        computadoras = list(self.db.computadoras.find())
        for computadora in computadoras:
            computadora["_id"] = str(computadora["_id"])  # Convertimos ObjectId a string
        return jsonify(computadoras)

    def obtener_computadora(self, id):
        computadora = self.db.computadoras.find_one({"_id": ObjectId(id)})
        if computadora:
            return jsonify({
                "_id": str(computadora["_id"]),
                "marca": computadora["marca"],
                "modelo": computadora["modelo"],
                "procesador": computadora["procesador"],
                "ram": computadora["ram"],
                "almacenamiento": computadora["almacenamiento"],
                "precio": computadora["precio"],
                "tarjeta_grafica": computadora.get("tarjeta_grafica", ""),
                "pantalla": computadora.get("pantalla", ""),
                "peso": computadora.get("peso", ""),
                "anio_lanzamiento": computadora.get("anio_lanzamiento", ""),
                "color": computadora.get("color", ""),
                "sistema_operativo": computadora.get("sistema_operativo", ""),
                "conectividad": computadora.get("conectividad", {}),
                "puertos": computadora.get("puertos", {}),
                "bateria": computadora.get("bateria", ""),
                "duracion_bateria": computadora.get("duracion_bateria", ""),
                "tipo_pantalla": computadora.get("tipo_pantalla", ""),
                "resolucion": computadora.get("resolucion", ""),
                "teclado": computadora.get("teclado", {}),
                "webcam": computadora.get("webcam", ""),
                "audio": computadora.get("audio", ""),
                "seguridad": computadora.get("seguridad", {}),
                "expansion": computadora.get("expansion", {}),
                "garantia": computadora.get("garantia", ""),
                "precio_venta": computadora.get("precio_venta", computadora["precio"]),
                "accesorios_incluidos": computadora.get("accesorios_incluidos", ""),
                "recomendado_para": computadora.get("recomendado_para", ""),
                "opiniones_usuarios": computadora.get("opiniones_usuarios", ""),
                "condicion": computadora.get("condicion", "Nuevo"),
                "fabricante_tarjeta_grafica": computadora.get("fabricante_tarjeta_grafica", "")
            }), 200
        return jsonify({"error": "Computadora no encontrada"}), 404

    def editar_computadora(self, id):
        data = request.get_json()

        computadora = self.db.computadoras.find_one({"_id": ObjectId(id)})
        if not computadora:
            return jsonify({"error": "Computadora no encontrada"}), 404

        # Actualizamos los datos con el nuevo contenido de `data` (si existe)
        self.db.computadoras.update_one(
            {"_id": ObjectId(id)}, 
            {"$set": {
                "marca": data.get("marca", computadora.get("marca")),
                "modelo": data.get("modelo", computadora.get("modelo")),
                "procesador": data.get("procesador", computadora.get("procesador")),
                "ram": data.get("ram", computadora. get("ram")),
                "almacenamiento": data.get("almacenamiento", computadora.get("almacenamiento")),
                "precio": data.get("precio", computadora.get("precio")),
                "tarjeta_grafica": data.get("tarjeta_grafica", computadora.get("tarjeta_grafica")),
                "pantalla": data.get("pantalla", computadora.get("pantalla")),
                "peso": data.get("peso", computadora.get("peso")),
                "anio_lanzamiento": data.get("anio_lanzamiento", computadora.get("anio_lanzamiento")),
                "color": data.get("color", computadora.get("color")),
                "sistema_operativo": data.get("sistema_operativo", computadora.get("sistema_operativo")),
                "conectividad": data.get("conectividad", computadora.get("conectividad")),
                "puertos": data.get("puertos", computadora.get("puertos")),
                "bateria": data.get("bateria", computadora.get("bateria")),
                "duracion_bateria": data.get("duracion_bateria", computadora.get("duracion_bateria")),
                "tipo_pantalla": data.get("tipo_pantalla", computadora.get("tipo_pantalla")),
                "resolucion": data.get("resolucion", computadora.get("resolucion")),
                "teclado": data.get("teclado", computadora.get("teclado")),
                "webcam": data.get("webcam", computadora.get("webcam")),
                "audio": data.get("audio", computadora.get("audio")),
                "seguridad": data.get("seguridad", computadora.get("seguridad")),
                "expansion": data.get("expansion", computadora.get("expansion")),
                "garantia": data.get("garantia", computadora.get("garantia")),
                "precio_venta": data.get("precio_venta", computadora.get("precio_venta")),
                "accesorios_incluidos": data.get("accesorios_incluidos", computadora.get("accesorios_incluidos")),
                "recomendado_para": data.get("recomendado_para", computadora.get("recomendado_para")),
                "opiniones_usuarios": data.get("opiniones_usuarios", computadora.get("opiniones_usuarios")),
                "condicion": data.get("condicion", computadora.get("condicion")),
                "fabricante_tarjeta_grafica": data.get("fabricante_tarjeta_grafica", computadora.get("fabricante_tarjeta_grafica"))
            }}
        )

        computadora_actualizada = self.db.computadoras.find_one({"_id": ObjectId(id)})

        return jsonify({
            "_id": str(computadora_actualizada["_id"]),
            "marca": computadora_actualizada["marca"],
            "modelo": computadora_actualizada["modelo"],
            "procesador": computadora_actualizada["procesador"],
            "ram": computadora_actualizada["ram"],
            "almacenamiento": computadora_actualizada["almacenamiento"],
            "precio": computadora_actualizada["precio"],
            "tarjeta_grafica": computadora_actualizada.get("tarjeta_grafica", ""),
            "pantalla": computadora_actualizada.get("pantalla", ""),
            "peso": computadora_actualizada.get("peso", ""),
            "anio_lanzamiento": computadora_actualizada.get("anio_lanzamiento", ""),
            "color": computadora_actualizada.get("color", ""),
            "sistema_operativo": computadora_actualizada.get("sistema_operativo", ""),
            "conectividad": computadora_actualizada.get("conectividad", {}),
            "puertos": computadora_actualizada.get("puertos", {}),
            "bateria": computadora_actualizada.get("bateria", ""),
            "duracion_bateria": computadora_actualizada.get("duracion_bateria", ""),
            "tipo_pantalla": computadora_actualizada.get("tipo_pantalla", ""),
            "resolucion": computadora_actualizada.get("resolucion", ""),
            "teclado": computadora_actualizada.get("teclado", {}),
            "webcam": computadora_actualizada.get("webcam", ""),
            "audio": computadora_actualizada.get("audio", ""),
            "seguridad": computadora_actualizada.get("seguridad", {}),
            "expansion": computadora_actualizada.get("expansion", {}),
            "garantia": computadora_actualizada.get("garantia", ""),
            "precio_venta": computadora_actualizada.get("precio_venta", computadora_actualizada["precio"]),
            "accesorios_incluidos": computadora_actualizada.get("accesorios_incluidos", ""),
            "recomendado_para": computadora_actualizada.get("recomendado_para", ""),
            "opiniones_usuarios": computadora_actualizada.get("opiniones_usuarios", ""),
            "condicion": computadora_actualizada.get("condicion", "Nuevo"),
            "fabricante_tarjeta_grafica": computadora_actualizada.get("fabricante_tarjeta_grafica", "")
        }), 200


    def eliminar_computadora(self, id):
        computadora = self.db.computadoras.find_one({"_id": ObjectId(id)})
        if not computadora:
            return jsonify({"error": "Computadora no encontrada"}), 404
        
        self.db.computadoras.delete_one({"_id": ObjectId(id)})
        
        return jsonify({"message": "Computadora eliminada exitosamente"}), 200
