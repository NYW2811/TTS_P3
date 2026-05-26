#importaciones
import time
import wave
import winsound

# funcion para la duracion del audio, evita que el programa se bloquee si el audio no se reproduce correctamente
def _duracion_audio(ruta):
    try:
        with wave.open(str(ruta), "rb") as archivo_audio:
            return archivo_audio.getnframes() / float(archivo_audio.getframerate())
    except wave.Error:
        return 1

# funcion para reproducir el audio, si no se reproduce correctamente, espera la duración del audio para evitar bloquearse
def reproducir_audio(indice, ruta, registro):
    registro.info("Reproduciendo fragmento %s", indice)

    try:
        winsound.PlaySound(str(ruta), winsound.SND_FILENAME)
    except RuntimeError:
        time.sleep(_duracion_audio(ruta))

    registro.info("Termino fragmento %s", indice)
