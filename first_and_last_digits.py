def find_digits(input_str):
    import re
    # Find all digits in the string
    digits = re.findall(r'\d', input_str)
    print(digits)
    if digits:
        first_digit = digits[0]
        last_digit = digits[-1]
        digit=int(str(first_digit)+str(last_digit))
        return digit
    else:
        print("No digits found in the string")


with open('digits_test_data.txt', 'r') as file:
    # Loop through each line in the file
    sum=0
    comma_separated_list=[]
    for line in file:
        stripped_line = line.strip()
        print(stripped_line)
        digit=find_digits(stripped_line)
        print(digit)
        sum+=digit
    print(sum)