def calculated_avarage(numbers):
    sum_elements=0
    avarege_list=[]
    for i,num in enumerate(numbers,start=1):
        sum_elements+=num
        runing_avarege=sum_elements/i
        avarege_list.append(runing_avarege)
    return avarege_list
a=list(map(int,input().split()))
print(calculated_avarage(a))
