from abc import ABC, abstractmethod

class BaseStage(ABC):
  """
  BaseStage is an abstract base class that defines the structure for processing stages.

  Methods
  -------
  __init__() -> None
    Initializes the BaseStage instance.
    
  process(image)
    Abstract method that processes an image. Must be implemented by subclasses.
  """


  def __init__(self) -> None:
    super().__init__()

  @abstractmethod
  def process(self, image):
    pass