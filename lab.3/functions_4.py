def is_prime(num):
   if num<2:
       return False
   for i in range(2,int(num**0.5)+1):
       if num%i==0:
           return False
   return True

def filter_primt(numbers):
    return [num for num in numbers if is_prime(num)]
numbers_list=list(map(int,input().split()))
result=filter_primt(numbers_list)
print(result)