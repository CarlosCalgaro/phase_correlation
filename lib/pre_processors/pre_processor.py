from abc import ABC, abstractmethod

class PreProcessor(ABC):
  """
  Abstract base class for pre-processing images.

  This class serves as a blueprint for creating pre-processors that can be used
  to process images before further analysis or processing. Subclasses must 
  implement the `process` method.

  Methods
  -------
  process(image)
    Abstract method to process an image. Must be implemented by subclasses.

  Attributes
  ----------
  None
  """

  def __init__(self) -> None:
    super().__init__()

  @abstractmethod
  def process(self, image):
    pass