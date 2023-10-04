import numpy as np

def vectorized_matrix_multiplication(A, B):
  """Computes the matrix multiplication of two numpy arrays.

  Args:
    A: A numpy array.
    B: A numpy array.

  Returns:
    A numpy array containing the matrix multiplication of A and B.
  """

  return np.matmul(A, B)

# Example usage:
output_matrix = vectorized_matrix_multiplication(input_matrix_1, input_matrix_2)
