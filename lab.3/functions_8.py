def spy_game(nums):
    a=" "
    for i in range(len(nums)):
        if nums[i]==0 or nums[i]==7:
            a=a+str(nums[i])
        else:
            continue
    if "007" in a:
        return True
    else:
        return False
nums=list(map(int,input().split()))
print(spy_game(nums))