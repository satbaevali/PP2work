def polindrom_word(word):
    elements_word=''.join(word.split()).lower()
    return elements_word==elements_word[::-1]

def unique_elements(nums):
    result=[]
    for i in nums:
        if i not in result:
            result.append(i)
    return result