from .pre_processor import PreProcessor

class RotatePreProcessor(PreProcessor):
  """
  RotatePreProcessor is a class that inherits from PreProcessor and is used to rotate an image by a specified angle.

  Attributes:
    angle (float): The angle by which the image will be rotated.

  Methods:
    __init__(angle):
      Initializes the RotatePreProcessor with the specified angle.
    
    process(image):
      Rotates the given image by the specified angle.

      Args:
        image (PIL.Image.Image): The image to be rotated.

      Returns:
        PIL.Image.Image: The rotated image.
  """

  def __init__(self, angle) -> None:
    self.angle = angle

  def process(self, image):
    return image.rotate(self.angle)