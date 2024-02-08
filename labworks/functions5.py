def is_prime(n):
    if n<2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def filter_prime(list_input):
    prime=[num for num in list_input if is_prime(num)]
    return prime
a=list(map(int,input().split()))
print(filter_prime(a))
        
    
        