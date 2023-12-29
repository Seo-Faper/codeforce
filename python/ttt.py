def count_characters(input_string):
    char_frequency = {}
    
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
            
    return char_frequency

input_string = input("문자열을 입력하세요: ")
result = count_characters(input_string)

for char, frequency in result.items():
    print(f"'{char}': {frequency}")
input_string2 = input("비교할 문자열을 입력하세요. :")
