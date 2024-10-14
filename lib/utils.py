import matplotlib.pyplot as plt
import numpy as np

def plot_images(images = [], titles = []):
  image_size = len(images)
  title_size = len(titles)
  if image_size != title_size:
    raise ValueError("Images and titles must have the same size")
  
  fig, axes = plt.subplots(1, image_size, figsize=(12, 6))
  
  for i in range(image_size):
    axes[i].imshow(images[i], cmap='gray', vmin=0, vmax=255)
    axes[i].axis('off')
    if titles[i]:
      axes[i].set_title(titles[i])
  plt.show()