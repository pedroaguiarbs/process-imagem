from PIL import Image
import numpy as np
from scipy.ndimage import median_filter
import matplotlib.pyplot as plt

image_path = 'atv-realce/salt_and_pepper.jpg'
image = Image.open(image_path).convert('L')  
image_array = np.array(image)

filtered_image_array = median_filter(image_array, size=3) 

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_array, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image_array, cmap='gray')
plt.title("Filtered Image (Median)")
plt.axis('off')

plt.show()
