PUERTO = 5555
TIEMPO_RONDA = 25
MAX_INTENTOS = 4
VALOR_INICIAL_PALABRA = 100
PENALIZACION_ERROR = 25
COSTO_PISTA_TEXTO = 10
COSTO_PISTA_LETRA = 15


NIVELES = {
    1: {
        "titulo": "🍔 Nivel 1: Comida Rápida",
        "items": [
            {
                "palabra": "HAMBURGUESA",
                "pistas": [
                    "Carne redonda a la parrilla servida dentro de un pan.",
                    "Suele llevar queso cheddar, lechuga, tomate y salsa."
                ]
            },
            {
                "palabra": "PIZZA",
                "pistas": [
                    "Masa horneada de origen italiano con forma circular.",
                    "Lleva salsa de tomate, queso derretido y pepperoni."
                ]
            },
            {
                "palabra": "TACOS",
                "pistas": [
                    "Platillo tradicional mexicano hecho con tortilla doblada.",
                    "Se rellena con carne asada, cilantro, cebolla y limón."
                ]
            },
            {
                "palabra": "HOTDOG",
                "pistas": [
                    "Pan alargado muy popular en puestos callejeros y estadios.",
                    "Lleva una salchicha caliente con kétchup y mostaza."
                ]
            },
            {
                "palabra": "NUGGETS",
                "pistas": [
                    "Bocados pequeños y crujientes hechos de pollo.",
                    "Son dorados por fuera y se comen mojados en salsas."
                ]
            }
        ]
    },
    2: {
        "titulo": "🍳 Nivel 2: Utensilios de Cocina",
        "items": [
            {
                "palabra": "SARTEN",
                "pistas": [
                    "Recipiente metálico plano con mango largo para la estufa.",
                    "Se usa para freír huevos, carnes o saltear verduras."
                ]
            },
            {
                "palabra": "CUCHILLO",
                "pistas": [
                    "Herramienta manual con mango y hoja metálica afilada.",
                    "Sirve para cortar, picar o rebanar alimentos."
                ]
            },
            {
                "palabra": "TENEDOR",
                "pistas": [
                    "Cubierto de mesa con mango y varias puntas metálicas.",
                    "Se usa para pinchar y llevar comida sólida a la boca."
                ]
            },
            {
                "palabra": "LICUADORA",
                "pistas": [
                    "Electrodoméstico con vaso alto y cuchillas en el fondo.",
                    "Tritura frutas y líquidos para hacer batidos o jugos."
                ]
            },
            {
                "palabra": "COLADOR",
                "pistas": [
                    "Utensilio con malla o muchos agujeros pequeños.",
                    "Separa líquidos de sólidos, como al escurrir pasta."
                ]
            }
        ]
    },
    3: {
        "titulo": "🦁 Nivel 3: Animales",
        "items": [
            {
                "palabra": "ELEFANTE",
                "pistas": [
                    "El mamífero terrestre más grande del planeta.",
                    "Tiene orejas enormes, colmillos de marfil y una larga trompa."
                ]
            },
            {
                "palabra": "COCODRILO",
                "pistas": [
                    "Reptil semiacuático grande con piel escamosa y dura.",
                    "Vive en ríos y pantanos, y tiene una mandíbula muy poderosa."
                ]
            },
            {
                "palabra": "PINGUINO",
                "pistas": [
                    "Ave marina que no puede volar, vestida de blanco y negro.",
                    "Nada a gran velocidad y vive en zonas muy frías como la Antártida."
                ]
            },
            {
                "palabra": "TIBURON",
                "pistas": [
                    "Depredador marino con esqueleto de cartílago y aleta dorsal.",
                    "Tiene varias filas de dientes afilados y un olfato increíble."
                ]
            },
            {
                "palabra": "CAMALEON",
                "pistas": [
                    "Reptil pequeño famoso por cambiar el color de su piel.",
                    "Mueve sus ojos por separado y caza insectos con su lengua larga."
                ]
            }
        ]
    }
}


def generar_pista_inicial(palabra):
    n = len(palabra)
    indices_visibles = {0, n - 1}
    if n >= 9:
        indices_visibles.add(n // 2)
    return [c if i in indices_visibles else "_" for i, c in enumerate(palabra)]

def calcular_puntuacion(puntuacion_actual, acierto):
    if acierto:
        return puntuacion_actual

    return max(0, puntuacion_actual - PENALIZACION_ERROR)

def verificar_respuesta(intento, palabra_correcta):
    return intento == palabra_correcta

import random

def revelar_letra(pista_actual, palabra_actual):
    ocultas = [i for i, c in enumerate(pista_actual) if c == "_"]

    if not ocultas:
        return None

    idx = random.choice(ocultas)
    pista_actual[idx] = palabra_actual[idx]

    return idx