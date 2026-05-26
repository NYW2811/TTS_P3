from config import maximo_caracteres_fragmento


def _dividir_oraciones(texto):
    oraciones = []
    actual = []

    for caracter in texto:
        actual.append(caracter)
        if caracter in ".!?;:":
            oracion = "".join(actual).strip()
            if oracion:
                oraciones.append(oracion)
            actual = []

    restante = "".join(actual).strip()
    if restante:
        oraciones.append(restante)

    return oraciones


def dividir_texto(texto, maximo_caracteres=maximo_caracteres_fragmento):
    fragmentos = []
    actual = ""

    for oracion in _dividir_oraciones(texto):
        if len(oracion) > maximo_caracteres:
            if actual:
                fragmentos.append(actual)
                actual = ""

            palabras = oracion.split()
            fragmento_corto = []
            longitud_corta = 0

            for palabra in palabras:
                espacio_extra = 1 if fragmento_corto else 0
                nueva_longitud = longitud_corta + len(palabra) + espacio_extra

                if fragmento_corto and nueva_longitud > maximo_caracteres:
                    fragmentos.append(" ".join(fragmento_corto))
                    fragmento_corto = [palabra]
                    longitud_corta = len(palabra)
                else:
                    fragmento_corto.append(palabra)
                    longitud_corta = nueva_longitud

            if fragmento_corto:
                fragmentos.append(" ".join(fragmento_corto))
        elif not actual:
            actual = oracion
        elif len(actual) + 1 + len(oracion) <= maximo_caracteres:
            actual = f"{actual} {oracion}"
        else:
            fragmentos.append(actual)
            actual = oracion

    if actual:
        fragmentos.append(actual)

    return fragmentos
