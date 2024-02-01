a=int(input())
b=float(input())
c=a/(b*b)
if c>18.5 and c<25.5:
    print("Оптимальная масса")
elif c<18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")