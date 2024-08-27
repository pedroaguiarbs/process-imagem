from PIL import Image
import numpy as np

# Carregar a imagem fornecida e converter para escala de cinza
imagem = Image.open('atv4/ondas.jpg').convert('L')  # Converta para escala de cinza
imagem = np.array(imagem)

# Definir os kernels Sobel para a direção x e y
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

sobel_y = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]])

# Função para aplicar o filtro Sobel
def aplicar_sobel(imagem, kernel):
    altura, largura = imagem.shape
    resultado = np.zeros((altura, largura))

    # Aplica o filtro de convolução
    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            regiao = imagem[i-1:i+2, j-1:j+2]
            valor = np.sum(regiao * kernel)
            resultado[i, j] = min(max(valor, 0), 255)  # Clamping para valores entre 0-255

    return resultado

# Aplicar Sobel em x e y
gradiente_x = aplicar_sobel(imagem, sobel_x)
gradiente_y = aplicar_sobel(imagem, sobel_y)

sobel_combined = np.sqrt(gradiente_x**2 + gradiente_y**2)
sobel_combined = (sobel_combined / np.max(sobel_combined)) * 255  # Normalizar para 0-255

imagem_sobel = Image.fromarray(sobel_combined.astype(np.uint8))
imagem_sobel.save('atv4/imagem_sobel.jpg')
imagem_sobel.show()
