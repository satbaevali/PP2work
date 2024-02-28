import re
def capital_to_spaces(text):
    list_input=re.sub(r'[a-zа-яё])([A-ZА-ЯЁ])', r'\1 \2',text)
    #В данном случае, ([a-zа-яё]) - это первая группа, представляющая строчную букву, и ([A-ZА-ЯЁ]) - вторая группа, представляющая заглавную букву. Шаблон r'\1 \2' означает, что между строчной и заглавной буквой будет вставлен пробел.
    return list_input

print(capital_to_spaces(input()))