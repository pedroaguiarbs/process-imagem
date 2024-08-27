from PIL import Image

largura = 256
altura = 100

imagem_horizontal = Image.new('L', (largura, altura))

for x in range(largura):
    for y in range(altura):
        valor_cinza = int(255 * (x / (largura - 1)))
        imagem_horizontal.putpixel((x, y), valor_cinza)

imagem_horizontal.save('gradiente_horizontal.jpg')
