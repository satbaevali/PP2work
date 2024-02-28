import re 
def replace_calon(text):
    pattern=re.compile(r'[ ,.]')
    # compile-для того чтобы ищет объект например: ,.
    result=pattern.sub(':',text)
    #sub-для замена използоваль
    return result
print(replace_calon(input()))