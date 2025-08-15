from PIL import Image


diretorio = r'C:\Users\ResTIC16\Downloads\pompompurin\images.png'
og = Image.open(diretorio).convert("RGB")  # Converte para RGB
og.show()

def converter_para_cinza(imagem):
    largura, altura = imagem.size
    imagem_cinza = Image.new("L", (largura, altura))  # Escala de cinza

    for y in range(altura):
        for x in range(largura):
            r, g, b = imagem.getpixel((x, y))  # Agora retorna 3 valores
            valor_cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
            imagem_cinza.putpixel((x, y), valor_cinza)

    return imagem_cinza

imagem_cinza = converter_para_cinza(og)
imagem_cinza.show()
imagem_cinza.save(r'C:\Users\ResTIC16\Downloads\pompompurin\imagem_cinza.png')
def binarizar_imagem(imagem_cinza, limiar=127):
  largura, altura = imagem_cinza.size
  imagem_binaria = Image.new("1", (largura, altura))  # Binária

  for y in range(altura):
      for x in range(largura):
          valor_cinza = imagem_cinza.getpixel((x, y))
          valor_binario = 1 if valor_cinza > limiar else 0
          imagem_binaria.putpixel((x, y), valor_binario)

  return imagem_binaria

imagem_binaria = converter_para_cinza(og)
imagem_binaria.show()
imagem_binaria.save(r'C:\Users\ResTIC16\Downloads\pompompurin\imagem_binaria.png')
