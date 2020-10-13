#Biblioteca para abrir a imagem
import cv2
#Biblioteca para criar o Histocrama
import matplotlib.pyplot as mat

#Abre a imagem
img = cv2.imread('exemplo.jpg')
cv2.imshow("Imagem Original", img)

#Imagem resultado
imgResultado = img

#Inicia o Vetor com o resultado do Histograma com posições de 0 até 255
histogram = []
for i in range(256):
    histogram.append(0)

#Histograma do resultado
histogramR = []
for i in range(256):
    histogramR.append(0)

#Salva infos
altura = img.shape[0]
largura = img.shape[1]

# Total de pixels da Imagem (N)
N = altura * largura
#Niveis de intensidade que cada pixel pode assumir
L = 256 # 0 ~ 255

#Constroi o Histograma
for coluna in range(altura):
    for linha in range(largura):
        #Pega o valor da intensidade na posição 0 pois ele retorna no padrão BGR e queremos só 1 das camadas
        #Para contar quantas vezes aquela intensidade aparece na imagem
        K = img[coluna][linha][0]
        histogram[K] = histogram[K] + 1

#Monta a "Tabela" que ficará com o histograma
mat.xlabel("Intensidade")
mat.ylabel("Repetições")
mat.title("Histograma da Imagem")

#Monta Histograma Acumulado
hAcumulado = []
for i in range(256):
    #Pega quantidade no Histograma original
    valorAcumulado = histogram[i]
    if(i > 0):
        #Pega o Ultimo valor adicionado e incrementa(Acumula)
        valorAcumulado = valorAcumulado + hAcumulado[i - 1]
    hAcumulado.append(valorAcumulado)

#Monta o Pk (Da aula) Divisão do Histograma Acumulado pelo número de Pixels
Pk = []
for i in range(256):
    resultado = hAcumulado[i]/N
    Pk.append(resultado)

#Monta o K' que é resultado de Pk * Variações de intensidade - 1 -> 0 ~ 255 = 256 variações - 1 -> 255, então: Pk * 255
kLinha = []
for i in range(256):
    resultado = round(Pk[i]*L)
    kLinha.append(resultado)
    
#Monta nova imagem trocando K por K'
for linha in range(largura):
    for coluna in range(altura):
        #Valor do Pixel Atual
        valorAtual = img[coluna][linha][0]
        #Novo Valor calculado
        novoValor = kLinha[valorAtual]
        #Adiciona intensidade para cada 1 das 3 camadas BGR
        for c in range(3):
            imgResultado[coluna][linha][c] = novoValor

#Constroi o Histograma do Resultado
for linha in range(largura):
    for coluna in range(altura):
        #Pega o valor da intensidade na posição 0 pois ele retorna no padrão BGR e queremos só 1 das camadas
        #Para contar quantas vezes aquela intensidade aparece na imagem
        K = imgResultado[coluna][linha][0]
        histogramR[K] = histogramR[K] + 1

#Adiciona histogramas Origem e Resultado na "Tabela" criada
mat.plot(histogramR, color="blue")
mat.plot(histogram, color="red")

cv2.imshow("Imagem Equalizada", imgResultado)
mat.show()
#876350