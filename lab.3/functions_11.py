def polindrom_word(word):
    elements_word=''.join(word.split()).lower()
    return elements_word==elements_word[::-1]
element=input()
print(polindrom_word(element))
