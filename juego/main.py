import tkinter as tk
import random
import logica as motor  # Importa tu archivo de lógica tal cual
from ventana import Vista # Importa tu clase de interfaz

class Controlador:
    def __init__(self):
        # Variables exactas del archivo logica.py
        self.answer = random.choice(motor.words).upper()
        self.hint = ["_"] * len(self.answer)
        self.wrong_guesses = 0
        self.guessed_letters = set()
        
        # Inicia la interfaz
        self.vista = Vista()

        #record
        self.score = 0

        # Estado inicial en la pantalla
        self.vista.label_palabra.config(text=" ".join(self.hint))
        
        # Conecta la interfaz
        self.vista.btn_enviar.config(command=self.procesar_turno)
        self.vista.entrada_texto.bind('<Return>', self.procesar_turno)

    def procesar_turno(self, event=None):
        # Capturamos la entrada del usuario
        guess = self.vista.entrada_texto.get().lower()
        self.vista.entrada_texto.delete(0, tk.END)

        # Validaciones de tu lógica original
        if len(guess) != 1 or not guess.isalpha():
            self.vista.mostrar_mensaje("Entrada inválida", "Por favor, ingresa una letra.")
            return

        #Lógica de verificación
        if guess in self.answer.lower():
            for i in range(len(self.answer)):
                if self.answer[i].lower() == guess:
                    self.hint[i] = guess.upper()

            self.score += 5
            # Actualizar las líneas en la pantalla
            self.vista.mostrar_progreso(" ".join(self.hint))

            self.vista.actualizar_puntaje(self.score)
            
        else:
            self.wrong_guesses += 1
            # Dibujar la parte del cuerpo
            self.vista.dibujar_persona(self.wrong_guesses)
        
        self.verificar_estado()  # Verifica si el juego ha terminado después de un error

    def finalizar_interfaz(self):
        self.vista.entrada_texto.config(state=tk.DISABLED)
        self.vista.btn_enviar.config(state=tk.DISABLED)

    def verificar_estado(self):
        resultado = motor.verificar_estado(self.hint, self.wrong_guesses)
        
        if resultado == "WIN":
            self.score += 50
            self.vista.actualizar_puntaje(self.score)
            if self.vista.reinicio("¡GANASTE!", f"¡Felicidades! La palabra era: {self.answer}"):
                self.reiniciar_juego()
            else:
                self.finalizar_interfaz()
        
        elif resultado == "LOSE":
            if self.vista.reinicio("¡PERDISTE!", f"Lo siento, la palabra era: {self.answer}"):
                self.reiniciar_juego(resetear_puntaje=True)
            else:
                self.finalizar_interfaz()
    
    def reiniciar_juego(self, resetear_puntaje=False):
        # REINICIO DE LÓGICA
        self.answer = random.choice(motor.words).upper()
        self.hint = ["_"] * len(self.answer)
        self.wrong_guesses = 0
        self.guessed_letters = set()
        
        if resetear_puntaje:
            self.score = 0
            self.vista.actualizar_puntaje(self.score)

        # Llamamos al método que limpia el Canvas y botones
        self.vista.limpiar_pantalla()
        
        # Ponemos los nuevos guiones bajos en la pantalla
        self.vista.label_palabra.config(text=" ".join(self.hint))

    def ejecutar(self):
        self.vista.iniciar()

if __name__ == "__main__":
    app = Controlador()
    app.ejecutar()
