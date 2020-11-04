# -*- coding: utf-8 -*-
"""
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
"""

def can_be_partitioned(multiset):
  multiset.sort()
  index = 1
  while(index < len(multiset)-1):
    n = sum(multiset[-index:])
    for j in range(len(multiset)):     
      if sum(multiset[:j]) == n :
        return True
    if index == len(multiset):
      break
    index+=1
  
  return False
  

assert can_be_partitioned([15, 5, 20, 10, 35, 15, 10])
assert not can_be_partitioned([15, 5, 20, 10, 35])
assert can_be_partitioned([1, 1, 1, 1, 1, 1, 6])
