# -*- coding: utf-8 -*-
"""
This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.
"""

def can_color_graph(adjancency_matrix, k):
  max_adjancecies = 0 
  for row in adjancency_matrix:
    max_adjancecies = max(max_adjancecies,sum(row))
  
  return k > max_adjancecies

# Driver code
adjacency_matrix_1 = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
]
assert can_color_graph(adjacency_matrix_1, 4)
assert not can_color_graph(adjacency_matrix_1, 3)
