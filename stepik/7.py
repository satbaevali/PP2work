a=input()
if len(a)==5:
    reversed_number=int(a[::-1])
else:
    reversed_number=int(a[0]+a[-5:][::-1])
print(reversed_number)