from .pre_processor import PreProcessor

class GrayScalePreProcessor(PreProcessor):
  
  def process(self, image):
    return image.convert('L')
  
