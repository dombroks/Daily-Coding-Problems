# -*- coding: utf-8 -*-
"""
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""

def get_subset(array , k):
  if len(array) == 0:
    return None
  if array[0] == k:
    return [array[0]]
  
  first = get_subset(array[1:] , k - array[0])
  if first:
    return [array[0]] + first
  else:
    return get_subset(array[1:],k)



# Driver code
S  = [12,1,61,5,9,2]
k = 24 
print(get_subset(S,k))
