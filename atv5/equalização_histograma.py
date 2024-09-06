from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

image_path = 'atv5/astronauta.jpg'
image = Image.open(image_path)

# Converter para escala de cinza
gray_image = np.array(image.convert('L'))

# Calcular o histograma
hist, bins = np.histogram(gray_image.flatten(), 256, [0, 256])

# Calcular a Função Densidade de Probabilidade (FDP)
pdf = hist / np.sum(hist)

# Calcular a Função Distribuição Acumulada (FDA)
cdf = pdf.cumsum()

# Normalizar a FDA
cdf_normalized = cdf * 255 / cdf[-1]

# Equalização de histograma
equalized_image = np.interp(gray_image.flatten(), bins[:-1], cdf_normalized)
equalized_image = equalized_image.reshape(gray_image.shape)

# Plotar a imagem original e equalizada lado a lado
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Imagem Equalizada')
plt.axis('off')

plt.tight_layout()
plt.show()

# Salvar o histograma e outros dados relevantes
np.savetxt('histograma.csv', hist, delimiter=',')
np.savetxt('pdf.csv', pdf, delimiter=',')
np.savetxt('cdf_normalizado.csv', cdf_normalized, delimiter=',')