import unicodedata

#-------------------------------------------------------------------------------------
# Este archivo tiene las funciones para normalizar el texto y que funcione bien el tts
#--------------------------------------------------------------------------------------

def _reparar_texto_roto(texto):
    marcas_texto_roto = ("\u00c3", "\u00e2", "\u00f0")
    if not any(marca in texto for marca in marcas_texto_roto):
        return texto

    try:
        return texto.encode("latin1").decode("utf-8")
    except UnicodeError:
        return texto


def normalizar_texto(texto):
    texto = _reparar_texto_roto(texto)
    texto = texto.replace("user-profile-picture", " ")
    texto = texto.replace("\u201c", '"').replace("\u201d", '"')
    texto = texto.replace("\u2018", "'").replace("\u2019", "'")

    lineas = []
    for linea in texto.splitlines():
        linea = " ".join(linea.split())
        if not linea:
            continue
        if linea[-1] == ",":
            linea = linea[:-1]
        if linea[-1] not in ".!?;:":
            linea += "."
        lineas.append(linea)

    texto = " ".join(lineas)
    texto = "".join(
        " "
        if unicodedata.category(caracter).startswith("C") or unicodedata.category(caracter) == "So"
        else caracter
        for caracter in texto
    )
    return " ".join(texto.split())
