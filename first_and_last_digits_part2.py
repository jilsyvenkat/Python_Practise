def find_digits(input_str):
    import re
    # Find all digits in the string
    # input_str="7pqrstsixteen"
    number_words_to_digits = {
        # 'oneight':'18','twone': '21', 'threeight': '38','fiveight':'58','sevenine':'79','eightwo': '82',
        # 'eighthree':'83','nineight':'98',
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    }
    # input_str = input_str.replace('oneight','1')
    # input_str = input_str.replace('twone', '2')
    # input_str = input_str.replace('threeight', '3')
    # input_str = input_str.replace('fiveight','5')
    # input_str = input_str.replace('sevenine','7')
    # input_str = input_str.replace('eightwo', '8')
    # input_str = input_str.replace('eighthree','8')
    # input_str = input_str.replace('nineight','9')
    print("initial input_str", input_str)
    input_str = input_str.replace('oneight','18')
    input_str = input_str.replace('twone', '21')
    input_str = input_str.replace('threeight', '38')
    input_str = input_str.replace('fiveight','58')
    input_str = input_str.replace('sevenine','79')
    input_str = input_str.replace('eightwo', '82')
    input_str = input_str.replace('eighthree','83')
    input_str = input_str.replace('nineight','98')
    # tlctwone39zfdqtnjshzjrqkcdnjnszrdfive
    # zntoneightfour1lcbzfhm4msneight7
    pattern = re.compile('|'.join(number_words_to_digits.keys()))
    # Replace words with digits
    modified_str = pattern.sub(lambda match: number_words_to_digits[match.group(0)], input_str)

    # Find all digits
    print("input_str",input_str)
    print("modified_str",modified_str)
    digits = re.findall(r'\d', modified_str)
    print(digits)
    if digits:
        first_digit = digits[0]
        last_digit = digits[-1]
        digit=int(str(first_digit)+str(last_digit))
        # print(digit)
        return digit
    else:
        print("No digits found in the string")


with open('digits_test_data.txt', 'r') as file:
    # Loop through each line in the file
    t_sum = []
    comma_separated_list=[]
    for line in file:
        stripped_line = line.strip()
        digit=find_digits(stripped_line)
        t_sum.append(digit)
    print(sum(t_sum))