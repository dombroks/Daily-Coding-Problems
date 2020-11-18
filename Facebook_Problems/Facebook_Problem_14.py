
"""
This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
"""

def is_editable(array):
  counter = 0
  for i in range(len(array)-1):
    if array[i] > array[i+1]:
      counter += 1
  return counter < 2

assert not is_editable([10, 5, 1]) 
assert is_editable([10, 5, 7]) 
assert is_editable([1, 10, 5, 7])
