from .base_stage import BaseStage
class CropStage(BaseStage):
    """
    A stage in the image processing pipeline that crops an image to the specified width and height.
    Attributes:
        width (int): The desired width of the cropped image.
        height (int): The desired height of the cropped image.
    Methods:
        process(image):
            Crops the given image to the specified width and height, centered on the image.
            Args:
                image (PIL.Image.Image): The image to be cropped.
            Returns:
                PIL.Image.Image: The cropped image.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def process(self, image):
      width, height = image.size  
      left = (width - self.width) // 2
      upper = (height - self.height) // 2
      right = left + self.width
      lower = upper + self.height
      return image.crop((left, upper, right, lower))