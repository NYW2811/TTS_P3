import time


class Temporizador:
    def __init__(self):
        self.inicio = time.perf_counter()

    def transcurrido(self):
        return time.perf_counter() - self.inicio


def imprimir_resumen(registro, modo, cantidad_fragmentos, tiempo_total):
    registro.info(
        "Resumen %s: %s fragmentos procesados en %.2f segundos",
        modo,
        cantidad_fragmentos,
        tiempo_total,
    )
