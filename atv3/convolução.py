from PIL import Image
import numpy as np

# Função para aplicar convolução
def aplicar_convolucao(imagem, kernel):
    largura, altura = imagem.size
    pixels = np.array(imagem)
    
    k_h, k_w = kernel.shape
    
    nova_imagem = Image.new('L', (largura, altura))
    resultado = np.zeros((altura, largura))
    
    # Percorrer cada pixel da imagem (exceto bordas)
    for i in range(k_h // 2, altura - k_h // 2):
        for j in range(k_w // 2, largura - k_w // 2):
            soma = 0
            for ki in range(-k_h // 2, k_h // 2 + 1):
                for kj in range(-k_w // 2, k_w // 2 + 1):
                    soma += pixels[i + ki, j + kj] * kernel[ki + k_h // 2, kj + k_w // 2]
            resultado[i, j] = min(max(soma, 0), 255)  # Clamping para 0-255
    
    for i in range(altura):
        for j in range(largura):
            nova_imagem.putpixel((j, i), int(resultado[i, j]))
    
    return nova_imagem

imagem_original = Image.open('/home/pedroaguiarbs/Desktop/process-imagem/atv3/flash.jpg').convert('L')  # Convertendo para escala de cinza

kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

imagem_filtrada = aplicar_convolucao(imagem_original, kernel)

imagem_filtrada.save('imagem_filtrada.jpg')
imagem_filtrada.show()
