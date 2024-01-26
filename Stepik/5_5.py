def buble_sort(arr):
    n=len(arr)
    count_s=0
    for i in range (n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count_s+=1
                swapped=True
        if not swapped:
            break
    return arr,count_s
n=int(input())
ls=list(map(int,input().split()))
sorted_ls,count_s=buble_sort(ls)
print(" ".join(map(str,sorted_ls)))
print(count_s)
    