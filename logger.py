import logging
import time
from pathlib import Path

from config import archivo_log


tiempo_inicio = time.perf_counter()


class FormatoConTiempo(logging.Formatter):
    def format(self, registro):
        registro.transcurrido = f"{time.perf_counter() - tiempo_inicio:0.2f}s"
        return super().format(registro)


def obtener_logger(nombre="tts_streaming"):
    Path(archivo_log).parent.mkdir(parents=True, exist_ok=True)

    registro = logging.getLogger(nombre)
    registro.setLevel(logging.INFO)

    if registro.handlers:
        return registro

    formato = "%(asctime)s | +%(transcurrido)s | %(threadName)s | %(levelname)s | %(message)s"
    formateador = FormatoConTiempo(formato, datefmt="%H:%M:%S")

    manejador_archivo = logging.FileHandler(archivo_log, encoding="utf-8")
    manejador_archivo.setFormatter(formateador)

    manejador_consola = logging.StreamHandler()
    manejador_consola.setFormatter(formateador)

    registro.addHandler(manejador_archivo)
    registro.addHandler(manejador_consola)
    return registro
