import numpy as np
from PIL import Image

def rotate_image(image_path, angle):
    # Carregar a imagem
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)
    
    # Obter dimensões da imagem original
    h, w, _ = img_array.shape
    angle_rad = np.radians(angle)

    # Calcular dimensões da nova imagem (caso a rotação mude o tamanho necessário)
    new_w = int(abs(w * np.cos(angle_rad)) + abs(h * np.sin(angle_rad)))
    new_h = int(abs(w * np.sin(angle_rad)) + abs(h * np.cos(angle_rad)))

    # Criar nova imagem com fundo preto
    rotated_img = np.zeros((new_h, new_w, 3), dtype=np.uint8)

    # Centro da imagem original e rotacionada
    cx, cy = w // 2, h // 2
    ncx, ncy = new_w // 2, new_h // 2

    # Aplicar a rotação pixel a pixel
    for y in range(new_h):
        for x in range(new_w):
            # Coordenadas na imagem original
            old_x = int((x - ncx) * np.cos(-angle_rad) - (y - ncy) * np.sin(-angle_rad) + cx)
            old_y = int((x - ncx) * np.sin(-angle_rad) + (y - ncy) * np.cos(-angle_rad) + cy)

            # Verificar se o ponto está dentro da imagem original
            if 0 <= old_x < w and 0 <= old_y < h:
                rotated_img[y, x] = img_array[old_y, old_x]

    # Converter para formato de imagem e retornar
    return Image.fromarray(rotated_img)

# Caminho da imagem enviada e ângulo de rotação
uploaded_image_path = "atv-rotação/spider.jpg"
rotated_image = rotate_image(uploaded_image_path, 45)
rotated_image.show()
