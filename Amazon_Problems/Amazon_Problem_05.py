# -*- coding: utf-8 -*-
"""
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

def get_max_sum_subarray(arr):
  if not arr or max(arr) < 0:
      return 0

  current_max = arr[0]
  final_max = arr[0]

  for number in arr[1:]:
    current_max = max(number, current_max + number)
    final_max = max(current_max, final_max)

  return final_max
  
  
assert get_max_sum_subarray([34, -50, 42, 14, -5, 86]) == 137
assert get_max_sum_subarray([-5, -1, -8, -9]) == 0
