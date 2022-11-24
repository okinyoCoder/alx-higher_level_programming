#!/usr/bin/python3 
def square_matrix_simple(matrix=[]):
    m = []
    for row in range(len(matrix)):
        m_row = []
        for col in row:
            m_row.append(col[i]**2)
        m.append(m_row)
    return m
