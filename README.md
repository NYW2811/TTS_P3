# TTS streaming

Este proyecto lee un texto, lo divide en fragmentos y despues genera audio TTS por partes.
El archivo principal simula streaming ya que mientras reproduce un fragmento ya generado,
prepara el siguiente fragmento en segundo plano.

## Como ejecutar

En Windows no se necesita instalar nada extra para la voz del sistema.

Ejecutar el modo concurrente:

```bash
python main.py
```

Ejecutar el modo secuencial, sin concurrencia, para comparar eficacia:

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

## Logs y medicion

Los logs aparecen en consola y tambien se guardan en:

```text
logs/tts.log
```


## Trabajos futuros

Esto lo hice por que usando llms locales, considero la oportunidad de hacer un chatbot que pueda tener como esta mecanica de tts que parezca streaming, para poder tener una conversación fluida con el llm mediante audio, tambien es de mi interes usar un speach to text para tener algo cercano a una conversación de voz con un llm :)
