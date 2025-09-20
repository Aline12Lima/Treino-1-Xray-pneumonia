import cv2
import numpy as np
import os
import csv


def extrair_caracteristicas(caminho_imagem):
  
  # 1----> transforma em tons de cinza
  
    imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    if imagem is None:
        print(f"Aviso: Imagem não encontrada - {caminho_imagem}")
        return None
    
  # 2----> redimenciona para tamanho paadrao e app filtro que remove ruidos e talll....
    tamanho_padrao = (256, 256)
    imagem = cv2.resize(imagem, tamanho_padrao, interpolation=cv2.INTER_AREA)
    imagem_filtrada = cv2.medianBlur(imagem, 5)


  #3  ---> extrai a caracteristica da intensidade intensidade alta =img clara intensidade baixa = img escura
    intensidade_media = np.mean(imagem_filtrada)

  #4 ----> calcula o desvio padrão da intensidade mede a variaçã do brilho 
    intensidade_desvio_padrao = np.std(imagem_filtrada)

  #5 ----> converte para P&B
    _, imagem_binaria = cv2.threshold(imagem_filtrada, 127, 255, cv2.THRESH_BINARY)

  #6 ----> encontra bordas para facilitar o trabalho de formas
    contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    area_maxima = 0
    perimetro_maximo = 0

    if contornos:
        contorno_maior = max(contornos, key=cv2.contourArea)
        area_maxima = cv2.contourArea(contorno_maior)
        perimetro_maximo = cv2.arcLength(contorno_maior, True)

    caracteristicas = [
        intensidade_media,
        intensidade_desvio_padrao,
        area_maxima,
        perimetro_maximo
    ]

    return caracteristicas




caminho_dataset = 'dataset/chest_xray'
pastas_classes = ['NORMAL', 'PNEUMONIA']
nome_arquivo_csv = 'caracteristicas_dataset.csv'


with open(nome_arquivo_csv, 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['intensidade_media', 'intensidade_desvio_padrao', 'area_maxima', 'perimetro_maximo', 'classe'])

   
    for tipo_dataset in ['train', 'test']:
        for classe in pastas_classes:
            caminho_completo = os.path.join(caminho_dataset, tipo_dataset, classe)
            
            if not os.path.exists(caminho_completo):
                print(f"Aviso: Pasta não encontrada - {caminho_completo}. Pulando.")
                continue

            print(f"Processando imagens em: {caminho_completo}")

            for nome_arquivo in os.listdir(caminho_completo):
                caminho_imagem = os.path.join(caminho_completo, nome_arquivo)
                
              
                if os.path.isfile(caminho_imagem) and not nome_arquivo.startswith('.'):
                    caracteristicas = extrair_caracteristicas(caminho_imagem)

                    if caracteristicas is not None:
                       
                        caracteristicas.append(classe)
                        escritor.writerow(caracteristicas)

print(f"\nExtração de características concluída! Dados salvos em {nome_arquivo_csv}")