from .base_stage import BaseStage

class RotateStage(BaseStage):
  """
  RotateStage is a stage in the image processing pipeline that rotates an image by a specified angle.
  Attributes:
    angle (float): The angle by which to rotate the image.
  Methods:
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