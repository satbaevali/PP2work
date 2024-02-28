import re
def camel_to_snake(text):
    list_input=re.sub(r'([a-zа-яё])([A-ZА-ЯЁ])', r'\1_\2',text).lower()
    return list_input
print(camel_to_snake(input()))