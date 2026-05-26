from pathlib import Path

# Configuracion general para el programa 
ruta_base = Path(__file__).resolve().parent
carpeta_entrada = ruta_base / "input"
carpeta_logs = ruta_base / "logs"
carpeta_audio_temporal = ruta_base / "temp_audio"

archivo_entrada = carpeta_entrada / "texto.txt"
archivo_log = carpeta_logs / "tts.log"

maximo_caracteres_fragmento = 110
maximo_audios_pendientes = 2
tiempo_limite_tts = 30
velocidad_voz = 2

texto_ejemplo = """
Este es un lector TTS sencillo con simulacion de streaming.
Mientras se reproduce un fragmento, el programa genera el siguiente en segundo plano.
La idea es comparar el tiempo total contra una version secuencial sin concurrencia.
Puedes cambiar este texto creando el archivo input/texto.txt.
"""
