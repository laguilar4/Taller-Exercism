def abbreviate(words):
    palabras = words
    separar = palabras.replace('_', ' ').replace('-', ' ').split()
    acronimo = ""

    for i in separar:
        acronimo = acronimo + i[0].upper()
    return acronimo
