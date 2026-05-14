import tkinter as tk
from tkinter import messagebox 

class Vista:
    Ancho = 600
    Alto = 700  

    def __init__(self):
    
        self.root = tk.Tk()
        self.root.title("Ahorcado")
        self.root.geometry(f"{self.Ancho}x{self.Alto}")
        self.root.config(bg="#ffffff", relief="ridge", bd=10)

        self.label_score = tk.Label(self.root, text=f"Puntaje: 0", font=("courier", 12))

        self.label_score.pack(pady=10)

        # 1. Canvas (Reducimos su altura para que quepa lo demás abajo)
        self.canvas = tk.Canvas(self.root, width=self.Ancho, 
                                height=400, bg="#e7dbdb", 
                                highlightthickness=0)
        self.canvas.pack()
        self.dibujar_soporte()

        # Lineas para la palabra
        self.label_palabra = tk.Label(self.root, text="_ _ _", font=("Courier", 30))
        self.label_palabra.pack(pady=20) # El pack va en su propia línea

        # 2. Frame de Entrada (Ajustado el color y padding)
        self.frame_entrada = tk.Frame(self.root, bg="#4004e7", padx=10, pady=10)
        self.frame_entrada.pack(pady=10)

        # Etiqueta del cuadro de texto
        self.label_instruccion = tk.Label(self.frame_entrada, text="Ingresa una letra:", 
                                         font=("Arial", 14), bg="#4004e7", fg="white")
        self.label_instruccion.pack(side=tk.LEFT, padx=5)                     
 
        # Cuadro de texto
        self.entrada_texto = tk.Entry(self.frame_entrada, font=("Arial", 14), 
                                      width=5, justify="center")
        self.entrada_texto.bind("<Return>")  # Permite presionar Enter
        self.entrada_texto.pack(side=tk.LEFT, padx=5)
        self.entrada_texto.focus_set()

        # Botón adivinar
        self.btn_enviar = tk.Button(self.frame_entrada, text="Adivinar", font=("Arial", 12),
                                    bg="#f0f0f0", cursor="hand2")
        self.btn_enviar.pack(side=tk.LEFT, padx=5)

        # Boton para salir
        self.btn_salir = tk.Button(self.root, text="Salir", command=self.root.quit, 
                                   font=("Arial", 12), bg="#a5a5a5", padx=20, pady=5, cursor="hand2")
        self.btn_salir.pack(pady=20)

    def dibujar_soporte(self):
        # Base
        self.canvas.create_line(50, 380, 150, 380, width=10, fill="#70492E")
        # Poste
        self.canvas.create_line(100, 380, 100, 50, width=5, fill="#70492E")
        # Viga
        self.canvas.create_line(98, 50, 253, 50, width=5, fill="#70492E")
        # Soga
        self.canvas.create_line(250, 50, 250, 100, width=5, fill="#636363")
    
    def mostrar_progreso(self, texto):
        self.label_palabra.config(text=texto)
    
    def dibujar_persona(self , errores): 
        if errores >= 1:  # Cabeza
            self.canvas.create_oval(230, 100, 270, 140, width=3, outline="#333333", fill="#f0c9c9")
        if errores >= 2:  # Cuerpo
            self.canvas.create_line(250, 140, 250, 220, width=3, fill="#333333")
        if errores >= 3:  # Brazo izquierdo
            self.canvas.create_line(250, 160, 220, 190, width=3, fill="#333333")
        if errores >= 4:  # Brazo derecho
            self.canvas.create_line(250, 160, 280, 190, width=3, fill="#333333")
        if errores >= 5:  # Pierna izquierda
            self.canvas.create_line(250, 220, 220, 250, width=3, fill="#333333")
        if errores >= 6:  # Pierna derecha
            self.canvas.create_line(250, 220, 280, 250, width=3, fill="#333333")
    
    def limpiar_pantalla(self):
        self.canvas.delete("all")
        self.dibujar_soporte()
        self.label_palabra.config(text="")
        self.entrada_texto.config(state=tk.NORMAL)  # Habilita la entrada de texto
        self.entrada_texto.delete(0, tk.END)
        self.btn_enviar.config(state=tk.NORMAL)  # Habilita el botón de enviar

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def reinicio(self, titulo, mensaje):
        respuesta = messagebox.askyesno(titulo, mensaje + "\n¿Quieres jugar de nuevo?")
        return respuesta
    
    def actualizar_puntaje(self, puntaje):
        self.label_score.config(text=f"Puntaje: {puntaje}")
    
    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Vista()
    app.iniciar()
