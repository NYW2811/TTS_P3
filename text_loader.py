from config import archivo_entrada, texto_ejemplo

# esta funcion carga el texto del archivo de entrada y si no existe crea uno con un default definido en ./config.py
def cargar_texto():
    archivo_entrada.parent.mkdir(parents=True, exist_ok=True)

    if not archivo_entrada.exists():
        archivo_entrada.write_text(texto_ejemplo.strip() + "\n", encoding="utf-8")

    return archivo_entrada.read_text(encoding="utf-8").strip()
