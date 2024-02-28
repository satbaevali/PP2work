import re
def string_input(text):
    pattern=re.compile(r'a.*b$')
    if pattern.match(text):
        return True
    else:
        return False
print(string_input(input()))