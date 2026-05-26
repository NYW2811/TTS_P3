import time
import wave
import winsound


def _duracion_audio(ruta):
    try:
        with wave.open(str(ruta), "rb") as archivo_audio:
            return archivo_audio.getnframes() / float(archivo_audio.getframerate())
    except wave.Error:
        return 1


def reproducir_audio(indice, ruta, registro):
    registro.info("Reproduciendo fragmento %s", indice)

    try:
        winsound.PlaySound(str(ruta), winsound.SND_FILENAME)
    except RuntimeError:
        time.sleep(_duracion_audio(ruta))

    registro.info("Termino fragmento %s", indice)
