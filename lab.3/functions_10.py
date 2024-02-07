def unique_elements(nums):
    result=[]
    for i in nums:
        if i not in result:
            result.append(i)
    return result
input_list=list(map(int,input().split()))
print(unique_elements(input_list))