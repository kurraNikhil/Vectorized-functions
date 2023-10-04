import numpy as np

def vectorized_box_muller(n):
  """Generates a vector of n standard normal variates using the Box-Müller method.

  Args:
    n: The number of normal variates to generate.

  Returns:
    A numpy array of n standard normal variates.
  """

  u = np.random.uniform(0, 1, size=n)
  v = np.random.uniform(0, 1, size=n)
  z = np.sqrt(-2 * np.log(u)) * np.cos(2 * np.pi * v)
  return z

# Example usage:
normal_variates = vectorized_box_muller(10000)
