
import numpy as np

class Comparator:

  def __init__(self, image1, image2):
    self.image1 = image1
    self.image2 = image2
  
  def compare(self):
    m1 = np.fft.fft2(self.image1)
    m2 = np.fft.fft2(self.image2)

    # Step 1: Compute the element-wise multiplication with conjugate
    tmp = m2 * np.conj(m1)

    # Step 2: Normalize by dividing by the absolute value
    normalized_r = tmp / np.abs(tmp)

    r = np.real(np.fft.ifft2(normalized_r))
    rho_chapeu, theta_chapeu = np.unravel_index(np.argmax(r), r.shape)
    return rho_chapeu, theta_chapeu