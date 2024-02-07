def tempereture(F):
    centigrade=((5/9)*(F-32))
    return centigrade
F=int(input())
result=tempereture(F)
print(result)