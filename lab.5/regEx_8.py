import re
def uppercase(text):
    input_string=re.findall('[A-Z][a-z]*',text)
    return input_string
print(uppercase(input()))