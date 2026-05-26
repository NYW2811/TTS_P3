from logger import obtener_logger
from stats import Temporizador, imprimir_resumen
from text_loader import cargar_texto
from text_processor import normalizar_texto
from text_splitter import dividir_texto
from workers import ejecutar_streaming


def main():
    registro = obtener_logger()
    temporizador = Temporizador()

    texto = normalizar_texto(cargar_texto())
    fragmentos = dividir_texto(texto)

    registro.info("Inicio modo concurrente/streaming con %s fragmentos", len(fragmentos))
    registro.info("Primer fragmento: %s", fragmentos[0] if fragmentos else "sin texto")
    ejecutar_streaming(fragmentos, registro)
    imprimir_resumen(registro, "concurrente", len(fragmentos), temporizador.transcurrido())


if __name__ == "__main__":
    main()
