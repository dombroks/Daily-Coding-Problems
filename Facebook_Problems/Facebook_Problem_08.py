# -*- coding: utf-8 -*-
"""
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

def get_maximum_profit(arr):
  list=[]
  max = 0
  for i in range(len(arr)):
    temp = arr[i]
    for j in range(i,len(arr)):
      if arr[j] > temp : 
        list.append((temp,arr[j]))

  for v1,v2 in list:
    if v2 - v1 > max:
      max = v2 - v1
  
  return max
    


assert get_maximum_profit([9, 11, 8, 5, 7, 10]) == 5
