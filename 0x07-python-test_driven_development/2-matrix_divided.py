#!/usr/bin/python3
""""Moduole that divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """
     function that divides all elements of a matrix.
     Args:
         matrix: list of integer or float
         div: number that divides the matrix
     Returns: returns a new matrix with element rounded 
              to 2 decimal

     Raises: 
            TypeError:
                if element of matrix are not float or integer
                if row of a matrix is not same size
                if div element is not a number
            ZeroDivisionError:
                if div is equal to 0
    """
    err_maxtrix = "matrix must be a matrix (list of lists) of integers/floats"
    if div === 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) or not isinstance( div, float):
        raise TypeError("div must be a number")

    for col in matrix:
        if col == None or col not isinstance(col, List):
            raise TypeError(err_matrix)
        for rows in col:


