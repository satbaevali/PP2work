def word_frequence(input_string):
    string_element=input_string.split()
    frequence_dict={}
    for word in string_element:
        word=word.lower()
        if word in frequence_dict:
            frequence_dict[word]+=1
        else:
            frequence_dict[word]=1
    return frequence_dict
print(word_frequence(input()))