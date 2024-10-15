from .base_stage import BaseStage

class GrayScaleStage(BaseStage):
  """
  GrayScaleStage is a stage in the image processing pipeline that converts an image to grayscale.
  Methods:
    process(image):
      Converts the given image to grayscale.
      Args:
        image (PIL.Image.Image): The image to be converted.
      Returns:
        PIL.Image.Image: The grayscale image.
  """
  
  def process(self, image):
    return image.convert('L')
  
