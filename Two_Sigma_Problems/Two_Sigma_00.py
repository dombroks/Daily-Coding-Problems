
"""
This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""

import random

def rand5():
  return random.randint(1,5)

def rand7():
  return random.randint(rand5(),7)


# Driver code
print(rand7())
