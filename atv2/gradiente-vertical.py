from PIL import Image

largura = 100
altura = 256

imagem_vertical = Image.new('L', (largura, altura))

for y in range(altura):
    for x in range(largura):
        valor_cinza = int(255 * (y / (altura - 1)))
        imagem_vertical.putpixel((x, y), valor_cinza)

imagem_vertical.save('gradiente_vertical.jpg')
