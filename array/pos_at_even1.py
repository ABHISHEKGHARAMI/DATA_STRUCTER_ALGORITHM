#pos element at the even place and neg element at the odd palce
array_nums = [1, -3, 5, 6, -3, 6, 7, -4, 9, 10]
print("Original arrays:")
print(array_nums)
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print("\nRearrange positive and negative numbers of the said array:")
print(result)
