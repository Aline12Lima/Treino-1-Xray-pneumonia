import cv2
import numpy as np
import os

def extrair_caracteristicas(caminho_imagem):
    """
    Processa uma imagem e extrai características numéricas.
    Entrada: caminho para o arquivo de imagem.
    Saída: uma lista de características (por exemplo, a área dos contornos).
    """
    imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)

    if imagem is None:
        print(f"Erro: Não foi possível ler a imagem em {caminho_imagem}.")
        return None  # Retorna None se a imagem não for encontrada

    # Segmentação da imagem
    _, imagem_segmentada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY_INV)

    # Encontra os contornos
    contornos, _ = cv2.findContours(imagem_segmentada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    dados_extraidos = []
    for contorno in contornos:
        if cv2.contourArea(contorno) > 50:
            area = cv2.contourArea(contorno)
            dados_extraidos.append([area])

    return dados_extraidos