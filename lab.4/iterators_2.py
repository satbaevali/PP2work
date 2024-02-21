def even_num(n):
    for i in range(0,n,2):
            yield i
n=int(input())
evens = even_num(n)
print({','.join(map(str,evens))})