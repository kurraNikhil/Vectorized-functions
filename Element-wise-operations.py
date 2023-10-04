import numpy as np

def vectorized_element_wise_add(x, y):
  """Adds two numpy arrays element-wise.

  Args:
    x: A numpy array.
    y: A numpy array.

  Returns:
    A numpy array containing the element-wise sum of x and y.
  """

  return x + y

def vectorized_element_wise_multiply(x, y):
  """Multiplies two numpy arrays element-wise.

  Args:
    x: A numpy array.
    y: A numpy array.

  Returns:
    A numpy array containing the element-wise product of x and y.
  """

  return x * y

# Example usage:
sum_matrix = vectorized_element_wise_add(matrix_1, matrix_2)
product_matrix = vectorized_element_wise_multiply(matrix_1, matrix_2)
