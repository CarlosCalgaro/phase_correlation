from .pre_processor import PreProcessor
"""
CropPreProcessor is a class that inherits from PreProcessor and is used to crop images to a specified width and height.

Attributes:
    width (int): The desired width of the cropped image.
    height (int): The desired height of the cropped image.

Methods:
    __init__(width, height):
        Initializes the CropPreProcessor with the specified width and height.
    
    process(image):
        Crops the given image to the specified width and height, centered on the image.
        Args:
            image (PIL.Image): The image to be cropped.
        Returns:
            PIL.Image: The cropped image.
"""

class CropPreProcessor(PreProcessor):
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