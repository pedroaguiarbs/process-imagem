from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np

image_path = 'atv-subtração-imagens/7_erros.jpg'
image = Image.open(image_path)

width, height = image.size
left_image = image.crop((0, 0, width // 2, height))
right_image = image.crop((width // 2, 0, width, height))

left_array = np.array(left_image)
right_array = np.array(right_image)

difference_array = np.abs(left_array - right_array)

threshold = 50  
highlighted_diff = np.where(difference_array > threshold, 255, 0).astype(np.uint8)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(left_image)
plt.title("Left Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(right_image)
plt.title("Right Image")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(highlighted_diff, cmap='gray')
plt.title("Highlighted Differences")
plt.axis('off')

plt.show()
