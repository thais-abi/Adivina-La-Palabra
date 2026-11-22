# Adivina-La-Palabra

Juego desarrollado en Python que permite adivinar palabras mediante pistas, con modalidad individual y multijugador a través de una conexión TCP/IP.

## Descripción del proyecto

Adivina la Palabra es un juego interactivo en el que los participantes deben descubrir palabras ocultas utilizando las pistas proporcionadas.

El juego cuenta con tres niveles temáticos:
Nivel 1: Comida rápida.
Nivel 2: Utensilios de cocina.
Nivel 3: Animales.

Cada palabra tiene un valor inicial de puntos. Los errores y el uso de pistas generan penalizaciones en la puntuación.

## Características principales

- Modalidad local (individual).
- Modalidad multijugador mediante red local (LAN).
- Comunicación entre jugadores mediante sockets TCP/IP.
- Sistema de puntuación y penalizaciones.
- Pistas de texto y revelación de letras.
- Temporizador por ronda.
- Interfaz gráfica interactiva.
- Efectos visuales, animaciones y sonidos.

## Tecnologías utilizadas

- Python.
- Tkinter para la interfaz gráfica.
- Sockets TCP/IP para la comunicación entre jugadores.
- JSON para el intercambio de mensajes.
- Threading para la ejecución de tareas simultáneas.

## Estructura del proyecto

El proyecto está organizado en cuatro archivos principales:

| Archivo | Descripción |

| `juego.py` | Contiene la interfaz gráfica, las animaciones y la coordinación de las partidas. |
| `server.py` | Gestiona la creación del servidor y la comunicación con los clientes. |
| `client.py` | Gestiona la conexión del jugador al servidor. |
| `game_logic.py` | Contiene las constantes, niveles y funciones de la lógica del juego. |

## Requisitos

- Python 3 instalado.
- Dos instancias del juego para probar el modo multijugador en un mismo equipo.
- Para jugar en equipos diferentes, ambos deben estar conectados a una red que permita la comunicación entre ellos.

## Instalación y ejecución

1. Descargar o clonar el repositorio.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
py juego.py
```

En algunos sistemas también puede utilizarse:

```bash
python juego.py
```

## Modalidades de juego

### Modo local

El jugador debe descubrir las palabras de cada nivel utilizando las pistas disponibles y administrando sus puntos e intentos.

### Modo multijugador

Un jugador inicia la partida como anfitrión (Host) y otro se conecta como cliente mediante la dirección IP del anfitrión.

## Autoría

Proyecto académico desarrollado por:

- Thaís Iza
- Mateo Rodriguez
- Odhalis Sanmartin

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para conocer sus condiciones de uso.

## Créditos y atribuciones

Actualmente, el proyecto no incorpora recursos externos que requieran atribución. Las bibliotecas y herramientas utilizadas pertenecen a sus respectivos autores.
