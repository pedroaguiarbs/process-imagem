from PIL import Image, ImageDraw

def bandeiraRussia(largura):
    proporcao = 2/3  
    altura = int(largura * proporcao)
    
    # Cores em RGB
    branco = (255, 255, 255)
    azul = (0, 57, 166)
    vermelho = (213, 43, 30)
    
    # Criar imagem
    bandeira = Image.new("RGB", (largura, altura))
    draw = ImageDraw.Draw(bandeira)
    
    # Desenhar as faixas
    altura_faixa = altura // 3
    draw.rectangle([0, 0, largura, altura_faixa], fill=branco)
    draw.rectangle([0, altura_faixa, largura, 2*altura_faixa], fill=azul)
    draw.rectangle([0, 2*altura_faixa, largura, altura], fill=vermelho)
    
    bandeira.show()

def bandeiraBelgica(largura):
    proporcao = 13/15  
    altura = int(largura * proporcao)
    
    # Cores em RGB
    preto = (0, 0, 0)
    amarelo = (255, 223, 0)
    vermelho = (239, 51, 64)
    
    # Criar imagem
    bandeira = Image.new("RGB", (largura, altura))
    draw = ImageDraw.Draw(bandeira)
    
    # Desenhar as faixas
    largura_faixa = largura // 3
    draw.rectangle([0, 0, largura_faixa, altura], fill=preto)
    draw.rectangle([largura_faixa, 0, 2*largura_faixa, altura], fill=amarelo)
    draw.rectangle([2*largura_faixa, 0, largura, altura], fill=vermelho)
    
    bandeira.show()

bandeiraRussia(300)  # Você pode ajustar a largura aqui
bandeiraBelgica(300)  # Você pode ajustar a largura aqui
