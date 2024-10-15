from lib.pipeline import Pipeline
from lib.stages import GrayScalePreProcessor, CropPreProcessor, RotateStage


NC, NL = 575, 575 
pipeline = Pipeline([
  GrayScalePreProcessor(),
  CropPreProcessor(NC, NL),
  RotateStage(45)
])

image = pipeline.execute()
