# -*- coding: utf-8 -*-
"""
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""

def pow(x,y):
	if y == 0:
		return 1
	if y == 1:
		return x
	if y == -1:
		return 1/x
	if y % 2 == 0:
		return pow(x,y/2) * pow(x,y/2)
	else:
		return x * pow(x,(y-1)/2) * pow(x,(y-1)/2)


assert pow(2,10) == 1024
assert pow(2,2) == 4
assert pow(3,2) == 9
assert not pow(2,7) == 1000
