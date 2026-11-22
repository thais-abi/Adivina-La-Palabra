
import socket


def conectar_servidor(ip, puerto):

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(5)
    cliente.connect((ip, puerto))
    cliente.settimeout(None)
    return cliente


def enviar_mensaje(cliente, mensaje, bloqueo):
    import json

    with bloqueo:
        datos = json.dumps(mensaje) + "\n"
        cliente.sendall(datos.encode("utf-8"))


def recibir_mensajes(conexion, seguir_escuchando, procesar_mensaje, al_desconectar):
    import json
    import socket

    buffer = ""

    try:
        while seguir_escuchando() and conexion:
            datos = conexion.recv(2048).decode("utf-8")

            if not datos:
                al_desconectar()
                break

            buffer += datos

            while "\n" in buffer:
                linea, buffer = buffer.split("\n", 1)

                if linea.strip():
                    mensaje = json.loads(linea)
                    procesar_mensaje(mensaje)

    except (ConnectionResetError, BrokenPipeError, OSError):
        al_desconectar()
