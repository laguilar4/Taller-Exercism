import re
from collections import Counter
def count_words(sentence):
    letras = re.findall(r"[a-z0-9]+'[a-z0-9]|[a-z0-9]+", sentence.lower())
    cont = Counter(letras)
    return cont
