# Adivina-La-Palabra

## Descripción del proyecto

Adivina-La-Palabra es un videojuego desarrollado en Python en el que los participantes deben descubrir palabras ocultas mediante pistas.

El juego está diseñado con tres niveles temáticos:

- **Nivel 1:** Comida rápida.
- **Nivel 2:** Utensilios de cocina.
- **Nivel 3:** Animales.

Cada palabra tiene un valor inicial de puntos. Los errores y el uso de pistas generan penalizaciones en la puntuación.

El proyecto contempla dos modalidades de juego: individual y multijugador mediante una conexión TCP/IP.

## Objetivo del proyecto

Desarrollar un videojuego interactivo que permita aplicar conceptos de programación, modularización, interfaces gráficas y comunicación entre dispositivos mediante sockets.

## Características del diseño

- Modalidad local (individual).
- Modalidad multijugador mediante red local (LAN).
- Comunicación entre jugadores mediante sockets TCP/IP.
- Sistema de puntuación y penalizaciones.
- Pistas de texto y revelación de letras.
- Temporizador por ronda.
- Interfaz gráfica interactiva.
- Efectos visuales, animaciones y sonidos.

Estas características corresponden al diseño general del videojuego y se implementarán progresivamente durante las etapas de desarrollo.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Tkinter:** biblioteca utilizada para desarrollar la interfaz gráfica.
- **Sockets TCP/IP:** comunicación entre servidor y cliente.
- **JSON:** intercambio de información entre los participantes.
- **Threading:** previsto para gestionar tareas simultáneas durante la integración del modo multijugador.
- **Git y GitHub:** control de versiones y alojamiento del repositorio.

## Estructura del proyecto

El proyecto está organizado en los siguientes archivos:

```text
Proyecto_AdivinaLaPalabra/
│
├── juego.py
├── server.py
├── client.py
├── game_logic.py
├── README.md
├── LICENSE
└── .gitignore
```

### Descripción de los archivos

- **juego.py:** contiene la interfaz gráfica principal y coordina los componentes del videojuego.
- **server.py:** administra la creación del servidor, la conexión de los clientes y la comunicación.
- **client.py:** permite establecer la conexión con el servidor y gestionar el intercambio de mensajes.
- **game_logic.py:** contiene las constantes, categorías, niveles, palabras, pistas y funciones relacionadas con la lógica del juego.
- **README.md:** presenta la documentación general del proyecto.
- **LICENSE:** contiene los términos de distribución y uso del proyecto.
- **.gitignore:** establece qué archivos deben excluirse del control de versiones.

## Estado actual del desarrollo

El proyecto se encuentra en su fase inicial de implementación correspondiente a la Fase 3.

Actualmente se cuenta con:

- Estructura modular de los archivos principales.
- Constantes, niveles, palabras y funciones iniciales de la lógica del juego.
- Funciones para establecer la comunicación mediante sockets TCP/IP.
- Mecanismos de envío y recepción de mensajes utilizando JSON.
- Una interfaz gráfica inicial desarrollada con Tkinter.
- Un menú principal con opciones para el modo local y multijugador.

En esta etapa, las opciones del menú muestran mensajes informativos. Las partidas completas y la integración funcional de ambas modalidades continuarán desarrollándose en las siguientes etapas.

## Requisitos

- Python 3 instalado.
- Tkinter disponible en la instalación de Python.
- Para probar el modo multijugador, se necesitarán dos instancias del juego y una conexión de red que permita la comunicación entre los equipos.

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

## Modalidades de juego previstas

### Modo local

El jugador deberá descubrir las palabras de cada nivel utilizando las pistas disponibles y administrando sus puntos e intentos.

### Modo multijugador

Un jugador podrá iniciar la partida como anfitrión (Host) y otro podrá conectarse como cliente mediante la dirección IP del anfitrión.

Ambas modalidades continuarán desarrollándose e integrándose durante las siguientes etapas.

## Autoría

Proyecto académico desarrollado por:

- Thaís Iza
- Mateo Rodriguez
- Odhalis Sanmartin

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para conocer sus condiciones de uso y distribución.

## Créditos y atribuciones

- **Bibliotecas:** se utilizan bibliotecas de Python, entre ellas Tkinter, socket, JSON y otras herramientas de la biblioteca estándar.
- **Inteligencia artificial:** se utilizó ChatGPT como herramienta de apoyo para la explicación de conceptos, orientación en la programación, revisión de código y organización de los módulos.
- **Recursos visuales:** la interfaz inicial utiliza elementos gráficos de Tkinter. No se han incorporado recursos visuales externos en esta versión inicial.

El código y los materiales del proyecto se desarrollan con fines académicos.