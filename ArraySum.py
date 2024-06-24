def arraySum(arr, index=0):
   if index == len(arr):
       return 0
   else:
       return arr[index] + arraySum(arr, index + 1)


print(arraySum([1,2,3,4,5]))