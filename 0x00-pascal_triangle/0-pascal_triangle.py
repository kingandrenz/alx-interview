#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    triangle = []

    if not isinstance(n, int) or n <= 0:
        """
        returns an empty list if n not an
        integer or less than 0
        """
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
