#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    """
    Generate Pascal's triangle with the specified number of rows.
    Returns a list of lists representing the triangle.
    """
    triangle = []

    if not isinstance(n, int) or n <= 0:

        return triangle
    else:
        for i in range(n):
            temp_list = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp_list.append(1)
                else:
                    temp_list.append(
                        triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(temp_list)

        return triangle
