import matplotlib.pyplot as plt
import numpy as np

# Define the images
img1 = np.array([
    [3, 3, 4, 4],
    [3, 4, 5, 4],
    [4, 5, 5, 3],
    [3, 4, 4, 5]
])

img2 = np.array([
    [2, 2, 5, 5],
    [2, 5, 7, 5],
    [5, 7, 7, 2],
    [2, 5, 5, 7]
])

img3 = np.array([
    [0, 0, 4, 4],
    [0, 4, 7, 4],
    [4, 7, 7, 0],
    [0, 4, 4, 7]
])

# Create the figure and subplots
plt.figure(figsize=(10, 8))

# Display image 1
plt.subplot(231)
plt.imshow(img1, cmap="gray", vmin=0, vmax=7)
plt.title("Image 1")

# Histogram of image 1
plt.subplot(234)
plt.hist(img1.ravel(), bins=8, range=(0,7), color='gray', rwidth=0.8)
plt.title("Histogram 1")

# Display image 2
plt.subplot(232)
plt.imshow(img2, cmap="gray", vmin=0, vmax=7)
plt.title("Image 2")

# Histogram of image 2
plt.subplot(235)
plt.hist(img2.ravel(), bins=8, range=(0,7), color='gray', rwidth=0.8)
plt.title("Histogram 2")

# Display image 3
plt.subplot(233)
plt.imshow(img3, cmap="gray", vmin=0, vmax=7)
plt.title("Image 3")

# Histogram of image 3
plt.subplot(236)
plt.hist(img3.ravel(), bins=8, range=(0,7), color='gray', rwidth=0.8)
plt.title("Histogram 3")

plt.tight_layout()
plt.show()
