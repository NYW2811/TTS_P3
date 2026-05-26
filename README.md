# TTS streaming simple con concurrencia

Este proyecto lee un texto, lo divide en fragmentos y genera audio TTS por partes.
El modo principal simula streaming: mientras reproduce un fragmento ya generado,
prepara el siguiente fragmento en segundo plano.

## Como ejecutarlo

En Windows no necesitas instalar nada extra para la voz del sistema.

Ejecuta el modo concurrente:

```bash
python main.py
```

Ejecuta el modo secuencial, sin concurrencia, para comparar eficacia:

```bash
python main_secuencial.py
```

## Texto de entrada

El programa busca el archivo:

```text
input/texto.txt
```

Si no existe, lo crea con un texto de ejemplo.

## Archivos importantes

- `main.py`: ejecuta el lector TTS concurrente tipo streaming.
- `main_secuencial.py`: ejecuta el lector sin concurrencia.
- `workers.py`: coordina productores, cola y reproduccion.
- `tts_engine.py`: genera los audios `.wav` con la voz del sistema de Windows.
- `audio_player.py`: reproduce los audios generados.
- `logger.py`: escribe logs con hora y tiempo transcurrido.
- `stats.py`: mide el tiempo total.
- `text_loader.py`, `text_processor.py`, `text_splitter.py`: cargan, reparan caracteres raros, limpian y dividen el texto.

## Concurrencia usada

El modo concurrente usa:

- `threading.Thread` para lanzar el productor de audio.
- `ThreadPoolExecutor` para generar fragmentos en segundo plano, usando un solo trabajador para evitar bloqueos del motor de voz.
- `queue.Queue` para pasar audios listos al reproductor.
- `Lock` para proteger el motor TTS, porque no conviene usarlo al mismo tiempo desde varios hilos.
- `Semaphore` para limitar cuantas tareas de generacion pueden estar activas.
- `Event` para avisar cuando el productor termino.

## Logs y medicion

Los logs aparecen en consola y tambien se guardan en:

```text
logs/tts.log
```

Cada linea incluye:

- Hora real.
- Tiempo transcurrido desde que inicio el programa.
- Nombre del hilo.
- Mensaje de generacion o reproduccion.

Al final se muestra un resumen con el tiempo total. Para comparar, ejecuta primero
`python main.py` y luego `python main_secuencial.py`.

## Nota

En Windows se genera la voz con `System.Speech` mediante PowerShell y se
reproduce con `winsound`. Si por alguna razon falla la generacion TTS real, el
programa crea un audio silencioso para que la ejecucion no se rompa. La
generacion tiene timeout para evitar que el programa se quede trabado. La
velocidad de voz se puede ajustar en `config.py` con `VOICE_RATE`.
