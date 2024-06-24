def remove_01_or_10(input_string):
    new_string = input_string
    print(new_string)
    while (new_string.find("01") != -1) or (new_string.find("10") != -1):
        new_string = new_string.replace("01","")
        new_string = new_string.replace("10", "")

    print(len(new_string))


# remove_01_or_10("ab1100cd3ef4+*gh5a10aa01bb10")
remove_01_or_10("01010")


