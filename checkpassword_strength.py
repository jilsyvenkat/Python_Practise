from collections import defaultdict
def multi_password_strength_counter(passwords):
    all_results = []
    special_characters = "!@#$%^&*()-+"
    special_char_list = list(special_characters)
    # print(special_char_list)
    # print(strength)
    # implement this
    for pwds in passwords:
        # print(pwds)
        strength = {
        'length': False,
        'digit': False,
        'lowercase': False,
        'uppercase': False,
        'specialchar': False
        }
        if len(pwds) >= 8:
            strength['length'] = True
        for char in pwds:
            if char.isdigit():
                strength['digit'] = True
            elif char.islower():
                strength['lowercase'] = True
            elif char.isupper():
                strength['uppercase'] = True
            elif char in special_char_list:
                strength['specialchar'] = True
        # print(strength)
        all_results.append(strength)
        # print(all_results[pwds])
    return all_results
    # return all_results

passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
# print(results)
for result in results:
    print(result)

# The expected output is:
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}