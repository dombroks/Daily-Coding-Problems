"""
This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

    (0, 0)
    (1, 2)
    (2, 2)
    (4, 0)

The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
"""


def bishops_under_attack(M, bishops):
    counter = 0

    for i in range(len(bishops)):
        pair = bishops[i]
        for j in range(i, len(bishops)):
            pair2 = bishops[j]
            if _are_in_the_same_diagonal(M, pair, pair2):
                counter += 1
    return counter


def _are_in_the_same_diagonal(matrix_length, pair1, pair2):
    if pair1 == pair2:
        return False
    diagonal = []
    second_diagonal = []
    for i in range(matrix_length):
        for j in range(matrix_length):
            if i == j:
                diagonal.append((i, j))
            if i + j == matrix_length - 1:
                second_diagonal.append((i, j))

    if pair1 in diagonal and pair2 in diagonal:
        return True
    if pair1 in second_diagonal and pair2 in second_diagonal:
        return True

    return False


# Driver code
bishops = [
    (0, 0),
    (1, 2),
    (2, 2),
    (4, 0)
]
assert bishops_under_attack(5, bishops) == 2
