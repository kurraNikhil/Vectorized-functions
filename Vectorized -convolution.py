import numpy as np

def vectorized_convolution(x, y):
  """Computes the convolution of two numpy arrays.

  Args:
    x: A numpy array.
    y: A numpy array.

  Returns:
    A numpy array containing the convolution of x and y.
  """

  return np.convolve(x, y, mode='same')

# Example usage:
filtered_image = vectorized_convolution(image, kernel)
