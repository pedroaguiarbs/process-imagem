import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

imagem = Image.open('atv-transf-fourier/spider.jpg').convert('L')
imagem = imagem.resize((100, 60))
imagem_np = np.array(imagem, dtype=float)
M, N = imagem_np.shape

imagem_deslocada = np.zeros((M, N), dtype=float)
for x in range(M):
    for y in range(N):
        imagem_deslocada[x, y] = imagem_np[x, y] * (-1)**(x + y)

fourier_transformada = np.fft.fft2(imagem_deslocada)
fourier_espectro = np.fft.fftshift(np.abs(fourier_transformada))

espectro_log = np.log(1 + fourier_espectro) * 30  

espectro_normalizado = (espectro_log - espectro_log.min()) / (espectro_log.max() - espectro_log.min())

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Imagem Original Deslocada")
plt.imshow(imagem_deslocada, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Espectro de Fourier (Log Ajustado e Normalizado)")
plt.imshow(espectro_normalizado, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
