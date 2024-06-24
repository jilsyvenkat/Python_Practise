def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorials(nums):
    # implement this
    new_list = []
    for i in nums:
        if i <0 :
            new_list.append('Error')
        else:
            val = factorial(i)
            new_list.append(val)
    return new_list
# def factorials(nums):
#     return [factorials(num) if factorials(num) is not None else 'Error' for num in nums]

print(factorials([2, 3, 4])) # should print: [2, 6, 24]
print(factorials([1, 5, 6])) # should print: [1, 120, 720]
print(factorials([0, -3, 10])) # should print: [1, 'Error', 3628800]