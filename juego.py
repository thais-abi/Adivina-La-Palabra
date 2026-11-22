import tkinter as tk
from tkinter import messagebox

from game_logic import (
    PUERTO,
    TIEMPO_RONDA,
    MAX_INTENTOS,
    VALOR_INICIAL_PALABRA,
    PENALIZACION_ERROR,
    COSTO_PISTA_TEXTO,
    COSTO_PISTA_LETRA,
    NIVELES,
    generar_pista_inicial,
    calcular_puntuacion,
    verificar_respuesta,
    revelar_letra
)

from server import (
    crear_servidor,
    esperar_cliente,
    enviar_mensaje as enviar_mensaje_servidor,
    recibir_mensajes as recibir_mensajes_servidor
)

from client import (
    conectar_servidor,
    enviar_mensaje as enviar_mensaje_cliente,
    recibir_mensajes as recibir_mensajes_cliente
)


class JuegoVisual:

    def __init__(self, root):
        self.root = root
        self.root.title("Adivina la Palabra — Royale Edition")
        self.root.geometry("690x730")
        self.root.resizable(False, False)
        self.root.configure(bg="#17152B")

        self.modo = None
        self.sock = None
        self.conn = None

        self.mostrar_menu()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_menu(self):
        self.limpiar_ventana()

        titulo = tk.Label(
            self.root,
            text="ADIVINA LA PALABRA",
            font=("Arial", 25, "bold"),
            bg="#17152B",
            fg="white"
        )
        titulo.pack(pady=50)

        subtitulo = tk.Label(
            self.root,
            text="ROYale EDITION",
            font=("Arial", 15),
            bg="#17152B",
            fg="#F5C542"
        )
        subtitulo.pack(pady=10)

        boton_local = tk.Button(
            self.root,
            text="MODO LOCAL",
            font=("Arial", 14, "bold"),
            width=20,
            command=self.iniciar_modo_solo
        )
        boton_local.pack(pady=20)

        boton_multijugador = tk.Button(
            self.root,
            text="MODO MULTIJUGADOR",
            font=("Arial", 14, "bold"),
            width=20,
            command=self.mostrar_menu_multijugador
        )
        boton_multijugador.pack(pady=10)

    def iniciar_modo_solo(self):
        self.modo = "solo"
        messagebox.showinfo(
            "Modo local",
            "El modo local se desarrollará en la siguiente etapa."
        )

    def mostrar_menu_multijugador(self):
        self.modo = "multijugador"
        messagebox.showinfo(
            "Modo multijugador",
            "La conexión multijugador se desarrollará en la siguiente etapa."
        )


if __name__ == "__main__":
    ventana = tk.Tk()
    juego = JuegoVisual(ventana)
    ventana.mainloop()
