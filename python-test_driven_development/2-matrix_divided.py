#!/usr/bin/python3

def custom_divid(a):
  return float("%0.2f" % a) 
def matrix_divided(matrix, div):
  #  if type(matrix) not in [int, float] or matrix != matrix:
 #       raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
  #  if type(div) not in [int, float] or div != div:
 #       raise TypeError("div must be a number")
#    if div == 0:
 #       raise ZeroDivisionError("division by zero")
    
    return [[custom_divid(item / div) for item in liste] for liste in matrix]
    