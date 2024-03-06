def sum_string(string):
    upper_sum=sum(1 for char in string if char.isupper())
    lower_sum=sum(1 for char in string if char.islower())
    return upper_sum,lower_sum
input_string=input()
upper,lower=sum_string(input_string)
print(f"upper_sum: {upper}, lower_sum:{lower}")
