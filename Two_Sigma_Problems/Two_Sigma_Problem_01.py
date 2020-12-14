
"""
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""

import random

def rand7():
  return random.randint(1,7)

def rand5():
  x = rand7()
  if x > 3:
   x -= 2 
  return random.randint(1,x)


# Driver code
print(rand5())
