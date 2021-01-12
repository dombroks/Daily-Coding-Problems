"""
This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

    init(arr, size): initialize with the original large array and size.
    set(i, val): updates index at i with val.
    get(i): gets the value at index i.

"""


class SparseArray:
    def __init__(self, arr, size):
        self.array = arr[:size]

    def set(self, i, val):
        self.array[i] = val

    def get(self, i):
        return self.array[i]


# Driver code
arr = [0, 5, 0, 48, 5, 36, 0, 0, 0, 0, 8, 215, 32, 75, 45, 94, 0, 0, 0]
sparse_array = SparseArray(arr, 11)
assert sparse_array.get(4) == 5
sparse_array.set(4, 10)
assert sparse_array.get(4) == 10
