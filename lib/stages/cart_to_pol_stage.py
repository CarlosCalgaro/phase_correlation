from .base_stage import BaseStage

import numpy as np

class CartToPolStage(BaseStage):
  """
  CartToPolStage class converts a Cartesian image to its polar representation.

  Attributes:
    dtheta (int): The angular resolution in degrees for the polar transformation.

  Methods:
    __init__(dtheta=1):
      Initializes the CartToPolStage with a given angular resolution.
    
    process(image):
      Converts the given Cartesian image to its polar representation.
      
      Args:
        image (array-like): The input Cartesian image.
      
      Returns:
        np.ndarray: The polar representation of the input image.
  """
  def __init__(self, dtheta = 1):
    self.dtheta = dtheta

  def process(self, image):
    image = np.array(image)
    width, height = image.shape
    Rho = int(np.floor(width // 2) - 1)
    theta_range = np.arange(0, 180, self.dtheta)
    print((Rho, len(theta_range)))
    polar_image = np.zeros((Rho, len(theta_range)))
    for rho in range(Rho):
        itheta = 0
        for theta in theta_range:
          nc = int(round(rho * np.sin(np.radians(theta)) + width / 2 + 1))
          nl = int(round(rho * np.cos(np.radians(theta)) + height / 2 + 1))
          if 1 <= nc < width and 1 <= nl < height:
            polar_image[rho, itheta] = image[nl, nc]
          itheta += 1
    return polar_image