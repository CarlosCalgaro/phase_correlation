from lib.pipeline import Pipeline
from lib.pre_processors import GrayScalePreProcessor, CropPreProcessor, RotatePreProcessor


NC, NL = 575, 575 
pipeline = Pipeline([
  GrayScalePreProcessor(),
  CropPreProcessor(NC, NL),
  RotatePreProcessor(45)
])

image = pipeline.execute()
