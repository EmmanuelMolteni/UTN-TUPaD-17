#main
from model.game_data import GameData
from logica import adivinar
from puntaje import contadorPuntaje

def AdivinanzasBinarias():
    print("Bienvenido a Adivinanzas Binarias")
    datos = GameData()
    
    for pregunta in datos.obtener_preguntas_y_respuestas:
        print("\n" + pregunta["pregunta"])
        
        opciones = "\n".join(pregunta["opciones"])
        print(opciones)
        
        if adivinar(pregunta["opciones"], pregunta["respuesta_correcta"]):
            print("Correcto!")
            contadorPuntaje()
        else:
            print("Incorrecto!")
            contadorPuntaje()
            
            #TODO: Hacer un contador de aciertos y fallos, en caso de que adivinar devuelva True, o False.
            
            #TODO: Hacer un contador de puntaje, el cual se calcula de la siguiente manera:
            # Si el jugador acierta, suma 10 puntos, si falla, resta 5 puntos. Si llega a 0 puntos, el juego termina.
            # El valor inicial del puntaje es de 15 puntos. Si llega a 0 puntos, el juego termina y si llega a superar los 70 puntos, el juego termina y el jugador gana.
            
if __name__ == "__main__":
    AdivinanzasBinarias()