from my_function import polindrom_word,unique_elements

word=input()
if polindrom_word(word):
    print("Yes")
else:
    print("No")

input_list=list(map(int,input().split()))
print(unique_elements(input_list))