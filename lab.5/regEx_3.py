import re

def find_sequences_with_underscore(input_string):
    pattern = r'\b[a-z]+_[a-z]+\b'
    matches = re.findall(pattern, input_string)
    return matches

input_text = "This is a sample_text with some_sequence and another_sequence_here."
sequences_with_underscore = find_sequences_with_underscore(input_text)

print("Sequences with underscore:", sequences_with_underscore)
