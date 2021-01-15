"""
This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

    init(size): initialize the array with size
    set(i, val): updates index at i with val where val is either 1 or 0.
    get(i): gets the value at index i.

"""


class BitArray:
    def __init__(self, size):
        self.arr = [0] * size

    def set(self, i, val):
        if val > 1 or val < 0:
            return
        self.arr[i] = val

    def get(self, i):
        if i > len(self.arr):
            return
        return self.arr[i]

    def __repr__(self):
        return str(self.arr)


# Driver code
bit_arr = BitArray(10)
assert bit_arr.get(7) == 0
assert bit_arr.get(100) is None
bit_arr.set(6, 1)
assert bit_arr.get(6) == 1
