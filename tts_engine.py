import math
import subprocess
import unicodedata
import wave

from config import carpeta_audio_temporal, tiempo_limite_tts, velocidad_voz


def _crear_wav_silencioso(ruta, segundos=1):
    frecuencia = 22050
    cuadros = b"\x00\x00" * math.ceil(segundos * frecuencia)

    with wave.open(str(ruta), "wb") as archivo_audio:
        archivo_audio.setnchannels(1)
        archivo_audio.setsampwidth(2)
        archivo_audio.setframerate(frecuencia)
        archivo_audio.writeframes(cuadros)


def _limpiar_para_voz(texto):
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ascii", "ignore").decode("ascii")

    caracteres_limpios = []
    for caracter in texto:
        categoria = unicodedata.category(caracter)
        if categoria.startswith("C") or categoria == "So":
            caracteres_limpios.append(" ")
        elif caracter in '"':
            caracteres_limpios.append("")
        else:
            caracteres_limpios.append(caracter)

    return " ".join("".join(caracteres_limpios).split())


def _generar_con_voz_windows(ruta, texto):
    ruta_texto = ruta.with_suffix(".txt")
    ruta_texto.write_text(_limpiar_para_voz(texto), encoding="utf-8")

    comando = (
        "& { param($rutaWav, $rutaTexto) "
        "Add-Type -AssemblyName System.Speech; "
        "$texto = [System.IO.File]::ReadAllText($rutaTexto, [System.Text.Encoding]::UTF8); "
        "$voz = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
        f"$voz.Rate = {velocidad_voz}; "
        "$voz.SetOutputToWaveFile($rutaWav); "
        "$voz.Speak($texto); "
        "$voz.Dispose(); "
        "}"
    )

    subprocess.run(
        ["powershell", "-NoProfile", "-Command", comando, str(ruta), str(ruta_texto)],
        check=True,
        timeout=tiempo_limite_tts,
        capture_output=True,
        text=True,
    )


def generar_audio(indice, texto, bloqueo_tts, registro):
    carpeta_audio_temporal.mkdir(parents=True, exist_ok=True)
    ruta = carpeta_audio_temporal / f"fragmento_{indice:03d}.wav"
    ruta_texto = ruta.with_suffix(".txt")

    registro.info("Generando fragmento %s", indice)

    with bloqueo_tts:
        try:
            ruta.unlink(missing_ok=True)
            ruta_texto.unlink(missing_ok=True)
            _generar_con_voz_windows(ruta, texto)
        except Exception as error:
            registro.warning("No se pudo generar TTS real (%s). Se crea audio silencioso.", error)
            _crear_wav_silencioso(ruta)

    registro.info("Fragmento %s listo: %s", indice, ruta.name)
    return indice, ruta
