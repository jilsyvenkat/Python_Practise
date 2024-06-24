# import re
#
#
# def solution(s1):
#     # Use regular expression to find old-style placeholders like %f, %s, etc.
#     s = re.sub(r'%[a-zA-Z%]', '{}', s1)
#     last_index = s.rfind('{}')
#
#     # If '{}' is found, replace it with '{}%'
#     if last_index != -1:
#         new_s = s[:last_index] + '%' + s[last_index + 2:]
#         return new_s
#     else:
#         # If '{}' is not found, return the original string
#         return s
#
#
#
# # Example usage
# s = "%d%d%%-growth in products is expected quite soon"
# new_format = solution(s)
# print("Old format:", s)
# print(new_format)

# def test_str(input_str):
#     input_str = "ABAB"
#     new_string = input_str.replace("A","B")
#     print(input_str)
#     print(new_string)
#     print(len(new_string))
#     x = len(new_string)
#     for i in range(0,x):
#         if input_str[i] == new_string[i]:
#             print("Replacing position : ",i, input_str[i])
#             left = new_string[:i]
#             right = new_string[i+1:]
#             new_string = left+"A"+right
#
#     print(new_string)
#
# test_str("Jilsy")


# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  # new_string = C.replace("A","B")
  new_string = C
  print(new_string)
  for i in range(0,N):
    # if C[i] == new_string[i]:
            print("Replacing position : ",i, C[i])
            left = new_string[:i]
            right = new_string[i+1:]
            if new_string[i] == "A":
                new_string = left+"B"+right
            else:
                new_string = left + "A" + right
  print(new_string)
  return new_string


getWrongAnswers(4,"ABAB")