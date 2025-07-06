"""❓ Problem Description:
Have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string "true" if any combination of numbers in the array (excluding the largest number) can be added up to exactly equal the largest number in the array.
Otherwise, return "false".
"""
#**********************************# checking if any combination can give add up to get the largest number 
from itertools import combinations

def ArrayAdditionI(arr):
    largest_number = max(arr)
    arr.remove(largest_number)

    # Try every combination of the remaining numbers
    for i in range(1, len(arr) + 1):
        for combo in combinations(arr, i):
            if sum(combo) == largest_number:
                return "true"
    
    return "false"

# Test
arr = [2, 7, 9, 11]
result = ArrayAdditionI(arr)
print(result)  # Output: "true" because 2 + 9 = 11



#**********************************# checking if 2 combination can give add up to get the largest number 
def ArrayAdditionI(arr):
    largest = max(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == largest:
                return arr[i], arr[j]

arr = [2, 7, 9, 11]      #largest = 11 , 9+2=11   
Result = ArrayAdditionI(arr)
print(Result)