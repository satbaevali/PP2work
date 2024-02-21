def returns_num(n):
    for i in range(n,0,-1):
        yield i
n=int(input())
for number in returns_num(n):
    print(number)
