import queue
import threading
from concurrent.futures import ThreadPoolExecutor

from audio_player import reproducir_audio
from config import maximo_audios_pendientes
from tts_engine import generar_audio


def ejecutar_streaming(fragmentos, registro):
    cola_audio = queue.Queue(maxsize=maximo_audios_pendientes)
    evento_fin = threading.Event()
    bloqueo_tts = threading.Lock()
    semaforo_generacion = threading.Semaphore(1)

    def productor():
        def generar_con_limite(indice, texto):
            with semaforo_generacion:
                return generar_audio(indice, texto, bloqueo_tts, registro)

        with ThreadPoolExecutor(max_workers=1, thread_name_prefix="tts") as ejecutor:
            for indice, texto in enumerate(fragmentos, start=1):
                futuro = ejecutor.submit(generar_con_limite, indice, texto)
                cola_audio.put(futuro.result())

        evento_fin.set()
        cola_audio.put(None)

    hilo_productor = threading.Thread(target=productor, name="productor-tts")
    hilo_productor.start()

    while not evento_fin.is_set() or not cola_audio.empty():
        elemento = cola_audio.get()
        if elemento is None:
            break

        indice, ruta = elemento
        reproducir_audio(indice, ruta, registro)
        cola_audio.task_done()

    hilo_productor.join()


def ejecutar_secuencial(fragmentos, registro):
    bloqueo_tts = threading.Lock()

    for indice, texto in enumerate(fragmentos, start=1):
        _, ruta = generar_audio(indice, texto, bloqueo_tts, registro)
        reproducir_audio(indice, ruta, registro)
