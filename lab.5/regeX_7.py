import re
def snake_to_camel(snake_case):
    words=re.split('_+',snake_case)
    camel_case=words[0]+''.join(word.capitalize() for word in words[1:])
    #word.capitalize(): Метод capitalize() преобразует первую букву слова в верхний регистр, а все остальные буквы делает строчными.
    return camel_case
print(snake_to_camel(input()))