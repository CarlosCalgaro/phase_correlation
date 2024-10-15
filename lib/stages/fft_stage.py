from .base_stage import BaseStage
import numpy as np

class FFTStage(BaseStage):
  """
  FFTStage is a class that performs a Fast Fourier Transform (FFT) on an input image and computes its magnitude spectrum.
  Attributes:
    apply_log (bool): A flag indicating whether to apply a logarithmic transformation to the magnitude spectrum.
  Methods:
    __init__(apply_log=True):
      Initializes the FFTStage with an optional parameter to apply logarithmic scaling.
    process(image):
      Performs a 2D FFT on the input image, shifts the zero-frequency component to the center, computes the magnitude spectrum, and optionally applies a logarithmic transformation.
      Args:
        image (numpy.ndarray): The input image on which to perform the FFT.
      Returns:
        numpy.ndarray: The magnitude spectrum of the FFT-transformed image, optionally scaled logarithmically.
  """

  def __init__(self, apply_log = True):
    self.apply_log = apply_log

  def process(self, image):
    # Perform 2D FFT
    fft2_result = np.fft.fft2(image)
    
    # Shift the zero-frequency component to the center of the spectrum
    fftshift_result = np.fft.fftshift(fft2_result)
    
    
    # Compute the magnitude spectrum
    magnitude_spectrum = np.abs(fftshift_result)
    
    if self.apply_log is True:
      # apply log10
      magnitude_spectrum = np.log10(magnitude_spectrum + 1e-21)  # Adding small constant to avoid log(0)
    
    return magnitude_spectrum