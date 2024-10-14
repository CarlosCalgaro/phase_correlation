class Pipeline:

  def __init__(self, stages):
    self.stages = stages
  
  def execute(self, image):
    for stage in self.stages:
      image = stage.process(image)
    return image