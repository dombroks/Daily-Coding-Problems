"""
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B

"""


def get_adj_pixels(pixel, matrix, rows, cols):
    adjacent_pixels = list()

    if pixel[0] > 0:
        adjacent_pixels.append((pixel[0] - 1, pixel[1]))
        if pixel[1] > 0:
            adjacent_pixels.append((pixel[0] - 1, pixel[1] - 1))
        if pixel[1] < cols - 1:
            adjacent_pixels.append((pixel[0] - 1, pixel[1] + 1))

    if pixel[0] < rows - 1:
        adjacent_pixels.append((pixel[0] + 1, pixel[1]))
        if pixel[1] > 0:
            adjacent_pixels.append((pixel[0] + 1, pixel[1] - 1))
        if pixel[1] < cols - 1:
            adjacent_pixels.append((pixel[0] + 1, pixel[1] + 1))

    if pixel[1] > 0:
        adjacent_pixels.append((pixel[0], pixel[1] - 1))

    if pixel[1] < cols - 1:
        adjacent_pixels.append((pixel[0], pixel[1] + 1))

    return adjacent_pixels


def change_color(pixel, matrix, new_color):
    if not matrix:
        return matrix

    x, y = pixel[0] - 1, pixel[1] - 1

    rows = len(matrix)
    cols = len(matrix[0])

    if x < 0 or y < 0 or x >= rows or y >= cols:
        return matrix

    c = matrix[x][y]
    adjacent_pixels = get_adj_pixels((x, y), matrix, rows, cols)

    for ap in adjacent_pixels:
        if matrix[ap[0]][ap[1]] == c:
            matrix[ap[0]][ap[1]] = new_color
    matrix[x][y] = new_color
    return matrix


# Driver code
matrix = [['B', 'B', 'W'],
          ['W', 'W', 'W'],
          ['W', 'W', 'W'],
          ['B', 'B', 'B']]
assert change_color((2, 2), matrix, 'G') == \
       [['B', 'B', 'G'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['B', 'B', 'B']]
