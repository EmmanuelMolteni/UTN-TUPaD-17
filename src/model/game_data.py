class GameData:
    def __init__(self):
        #Es un diccionario que contiene las preguntas y respuestas del juego, por favor sigan el mismo formato.
        self.preguntas_y_respuestas = [
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 1010",
                "opciones": ["A) 8", "B) 10", "C) 12", "D) 14"],
                "respuesta_correcta": ["B", "10"]
            },
            {
                "pregunta": "Prueba2",
                "opciones": ["A) 8", "B) 10"],
                "respuesta_correcta": ["A", "8"]
            },
        ]
        
    # Funcion para obtener las preguntas y respuestas del juego, es llamada desde el main.py
    # y es la que se encarga de devolver la lista de preguntas y respuestas.
    # Lo que permite property es que se pueda llamar a la funcion como un atributo, sin necesidad de usar parentesis
    @property
    def obtener_preguntas_y_respuestas(self):
        """Devuelve la lista de preguntas del juego"""
        return self.preguntas_y_respuestas