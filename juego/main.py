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
        
        # Estado inicial en la pantalla
        self.vista.label_palabra.config(text=" ".join(self.hint))
        
        # 4. Conecta la interfaz
        self.vista.btn_enviar.config(command=self.procesar_turno)
        self.vista.entrada_texto.bind('<Return>', self.procesar_turno)

    def procesar_turno(self, event=None):
        # Capturamos la entrada del usuario
        guess = self.vista.entrada_texto.get().lower()
        self.vista.entrada_texto.delete(0, tk.END)

        # Validaciones de tu lógica original
        if len(guess) != 1 or not guess.isalpha() or guess in self.guessed_letters:
            return

        self.guessed_letters.add(guess)

        #Lógica de verificación (manteniendo tus nombres de variables) ---
        if guess in self.answer.lower():
            for i in range(len(self.answer)):
                if self.answer[i].lower() == guess:
                    self.hint[i] = guess.upper()
            # Actualizar las líneas en la pantalla
            self.vista.mostrar_progreso(" ".join(self.hint))
        else:
            self.wrong_guesses += 1
            # Dibujar la parte del cuerpo
            self.vista.dibujar_persona(self.wrong_guesses)
        
        if self.wrong_guesses >= 6:  # Asumiendo que el límite es 6 errores
            self.wrong_guesses
            self.verificar_estado()  # Verifica si el juego ha terminado después de un error
  
        self.verificar_estado()

    def finalizar_interfaz(self):
        self.vista.entrada_texto.config(state=tk.DISABLED)
        self.vista.btn_enviar.config(state=tk.DISABLED)

#preguntar---------------
    def verificar_estado(self):
        if "_" not in self.hint:
            if self.vista.reinicio("¡GANASTE!", f"¡Felicidades! La palabra era: {self.answer}"):
                self.reiniciar_juego()
            else:
                self.finalizar_interfaz()
            
        elif self.wrong_guesses >= 6:  # Asumiendo que el límite es 6 errores
            if self.vista.reinicio("¡PERDISTE!", f"Lo siento, la palabra era: {self.answer}"):
                self.reiniciar_juego()
            else:
                self.finalizar_interfaz()
    
    def reiniciar_juego(self):
        # --- A. REINICIO DE LÓGICA ---
        # Elegimos nueva palabra usando tu módulo 'motor'
        self.answer = random.choice(motor.words).upper()
        self.hint = ["_"] * len(self.answer)
        self.wrong_guesses = 0
        self.guessed_letters = set()

        # --- B. REINICIO DE VISTA ---
        # Llamamos al método que limpia el Canvas y botones
        self.vista.limpiar_pantalla()
        
        # Ponemos los nuevos guiones bajos en la pantalla
        self.vista.label_palabra.config(text=" ".join(self.hint))
        
        # (Opcional) Un pequeño print para confirmar en consola
        print(f"Juego reseteado.")

    def ejecutar(self):
        self.vista.iniciar()

if __name__ == "__main__":
    app = Controlador()
    app.ejecutar()
