def square(a,b):
    for i in range(a,b+1):
        yield i**2
a,b=map(int,input().split())
numbers=square(a,b)
for number in numbers:
    print(number)