
import socket


def crear_servidor(puerto):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(("0.0.0.0", puerto))
    servidor.listen(1)

    return servidor


def esperar_cliente(servidor):
    conexion, direccion = servidor.accept()
    return conexion, direccion


def enviar_mensaje(conexion, mensaje, bloqueo):
    import json

    with bloqueo:
        datos = json.dumps(mensaje) + "\n"
        conexion.sendall(datos.encode("utf-8"))


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
