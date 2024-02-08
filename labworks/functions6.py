def find_common_elements(list1,list2):
    common_elements=[element for element in list1 if element in list2]
    return sorted(set(common_elements))
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
print(find_common_elements(list1,list2))