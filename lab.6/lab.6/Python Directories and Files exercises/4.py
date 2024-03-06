x = open("text.txt", 'r')
text = x.read()
r = text.count('\n')
print(r+1)