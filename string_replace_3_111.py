def replace_digit_with_countofones(input_string):
    new_string = input_string
    replace_with_1 = '1'
    digits_list = [1,2,3,4,5,6,7,8,9,0]
    print(new_string)
    for i in digits_list:
        new_string = new_string.replace(str(digits_list[i]),replace_with_1*digits_list[i])
    print(new_string)

replace_digit_with_countofones("ab2cd3ef4+*gh5a0")

