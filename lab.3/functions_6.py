def reversed_string(input_string):
    words=input_string.split()
    reversed_word=words[::-1]
    reversed_result=' '.join(reversed_word)
    return reversed_result
word=input()
print(reversed_string(word))