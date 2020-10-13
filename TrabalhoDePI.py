#Biblioteca para criar o Histograma
import matplotlib.pyplot as mat

#Inicializa valor iniciais dos pixels
pixels = []
maiorValor = 0

#Valores da aula(Para testes) - Necessario comentar ou remover o While de inserção
pixels = [0,0,4,6,8,8,4,7,8,9,9,4,3,2,3,8,2,2,1,0]
maiorValor = 9

#Começa loop para inserção dos Valores
i = 0

# Total de pixels da Imagem (N)
N = 20

#Monta a "Tabela" que ficará com o histograma
mat.xlabel("Intensidade")
mat.ylabel("Repetições")
mat.title("Histograma da Imagem")

pixelsEqualizados = [] #Inicializa Vetor resultado

#Niveis de intensidade que cada pixel pode assumir
L = maiorValor + 1 #Considera intensidade 0 por isso o + 1

#Inicia o Vetor com o resultado do Histograma com posições de 0 até até maior valor da intensidade
histogram = []
for i in range(L):
    histogram.append(0)
#Histograma do resultado
histogramR = []
for i in range(L):
    histogramR.append(0)

#Monta histograma dos inputs
for i in range(20):
    k = pixels[i]
    histogram[k] = histogram[k] + 1

#Monta Histograma Acumulado
hAcumulado = []
for i in range(L):
    #Pega quantidade no Histograma original
    valorAcumulado = histogram[i]
    if(i > 0):
        #Pega o Ultimo valor adicionado e incrementa(Acumula)
        valorAcumulado = valorAcumulado + hAcumulado[i - 1]
    hAcumulado.append(valorAcumulado)

#Monta o Pk Divisão do Histograma Acumulado pelo número de Pixels
Pk = []
for i in range(L):
    resultado = hAcumulado[i]/N
    Pk.append(resultado)

#Monta o K' que é resultado de Pk * Variações de intensidade
kLinha = []
for i in range(L):
    resultado = round(Pk[i]*maiorValor)
    kLinha.append(resultado)

for i in range(20):
    #Valor do Pixel Atual
    valorAtual = pixels[i]
    #Novo Valor calculado
    novoValor = kLinha[valorAtual]
    pixelsEqualizados.append(novoValor)

#Monta histograma do Resultado
for i in range(20):
    k = pixelsEqualizados[i]
    histogramR[k] = histogramR[k] + 1
print("No Histograma: O resultado está Azul e a Origem está vermelho")
print("--------------------------------------------------------------------------------------------------------------")
#Monta tabela para visualizar resultado
linha = ""
linha = linha + "k |"
for i in range(L):
    linha = linha + "\t" + str(i)+"|"
print(linha)

linha = ""
linha = linha + "H(k)|"
for i in range(L):
    linha = linha + "\t" + str(histogram[i])+"|"
print(linha)

linha = ""
linha = linha + "Ha(k)|"
for i in range(L):
    linha = linha + "\t" + str(hAcumulado[i])+"|"
print(linha)

linha = ""
linha = linha + "Pk|"
for i in range(L):
    linha = linha + "\t" + str(Pk[i])+"|"
print(linha)

linha = ""
linha = linha + "k'|"
for i in range(L):
    linha = linha + "\t" + str(kLinha[i])+"|"
print(linha)
print("--------------------------------------------------------------------------------------------------------------")
linha = ""
print("Entrada: ")
for i in range(20):
    linha = linha + "\t" + str(pixels[i])+"|"
print(linha)
print("--------------------------------------------------------------------------------------------------------------")
linha = ""
print("Saida: ")
for i in range(20):
    linha = linha + "\t" + str(pixelsEqualizados[i])+"|"
print(linha)
print("--------------------------------------------------------------------------------------------------------------")


#Adiciona histogramas Origem e Resultado na "Tabela" criada
mat.plot(histogramR, color="blue")
mat.plot(histogram, color="red")
mat.show()