import numpy as np

def vectorized_conditional_operation(condition, x, y):
  """Performs a conditional operation on two numpy arrays.

  Args:
    condition: A numpy array of booleans.
    x: A numpy array.
    y: A numpy array.

  Returns:
    A numpy array containing the result of the conditional operation.
  """

  return np.where(condition, x, y)

# Example usage:
output_matrix = vectorized_conditional_operation(condition_matrix, matrix_1, matrix_2)
