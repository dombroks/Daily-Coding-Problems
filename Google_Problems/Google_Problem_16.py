# -*- coding: utf-8 -*-
"""
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

Note added by me : Faster than O(N^2) means O(n log n) or faster if you could xD
"""

def merge_sort(arr):
  if not arr or len(arr) == 1 :
    return arr , 0

  middle = len(arr) // 2
  merged_array , inversions = merge(
      merge_sort(arr[:middle]) , merge_sort(arr[middle:]))
  return merged_array , inversions

def merge(pair1,pair2):
  i , k = 0, 0
  merged = list()
  a , a_inv = pair1
  b , b_inv = pair2
  inversions = a_inv + b_inv 

  while i < len(a) and k < len(b):
        if a[i] < b[k]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[k])
            inversions += len(a[i:])
            k += 1

  while i < len(a):
        merged.append(a[i])
        i += 1
  while k < len(b):
        merged.append(b[k])
        k += 1

  return merged, inversions


  
def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions


assert count_inversions([1, 2, 3, 4, 5]) == 0
assert count_inversions([2, 1, 3, 4, 5]) == 1
assert count_inversions([2, 4, 1, 3, 5]) == 3
assert count_inversions([2, 6, 1, 3, 7]) == 3
assert count_inversions([5, 4, 3, 2, 1]) == 10
