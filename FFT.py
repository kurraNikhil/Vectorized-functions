import numpy as np
from scipy.fftpack import fftn, ifftn

def vectorized_fft(x):
  """Computes the fast Fourier transform (FFT) of a numpy array.

  Args:
    x: A numpy array.

  Returns:
    A numpy array containing the FFT of x.
  """

  return fftn(x)

# Example usage:
fft_coefficients = vectorized_fft(image)
