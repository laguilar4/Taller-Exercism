def abbreviate(words):
    palabras = words
    dividirpalabras = palabras.replace('_', ' ').replace('-', ' ').split()
    acronimo = ""

    ## iterate through every substring
    for i in dividirpalabras:
        acronimo = acronimo + i[0].upper()
    return acronimo
