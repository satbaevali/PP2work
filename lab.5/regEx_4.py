import re
def find_sequences(text):
    pattern=re.compile(r'[A-Z][a-z]+')
    sequences=pattern.findall(text)
    return sequences
input_text=input()
print(find_sequences(input_text))