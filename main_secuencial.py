"""
Este archivo ejecuta de manera secuencial el programa principal
esto para tener una referencia de tiempo con y sin concurrencia
"""

from logger import obtener_logger
from stats import Temporizador, imprimir_resumen
from text_loader import cargar_texto
from text_processor import normalizar_texto
from text_splitter import dividir_texto
from workers import ejecutar_secuencial


def main():
    registro = obtener_logger()
    temporizador = Temporizador()

    texto = normalizar_texto(cargar_texto())
    fragmentos = dividir_texto(texto)

    registro.info("Inicio modo secuencial sin concurrencia con %s fragmentos", len(fragmentos))
    registro.info("Primer fragmento: %s", fragmentos[0] if fragmentos else "sin texto")
    ejecutar_secuencial(fragmentos, registro)
    imprimir_resumen(registro, "secuencial", len(fragmentos), temporizador.transcurrido())


if __name__ == "__main__":
    main()
