# Pesquisa_Cientifica_Biologia
Pesquisa Computação ML, voltada a visualização de dados Biologia
Neste projeto usei, VSCode. instalei o Python.
Usei as seguintes bibliotecas:
OpenCV, pip install opencv-contrib-python, **o openCv uso para processar as imagens, ler, converter e extrair caractersticas.** 

NumPy , pip install numpy, pip install numpy **ele manipula os arrays e cria também e esses arrays reprentam cada imagem.** 

Pandas,pip install pandas, **ela carrega e manipula os dados do arquivo .CSV e tranforma em table.**

Scikit-learn, pip install scikit-learn,  **essa é a minha biblioteca principal para ML, ela separa os dados de treino e teste, e treinma.**

jupyter,  é instalado tbm no terminal, ferranenta padrao do Python, para relaizar o treinamento da ML

# Resultados do Treinamento e Teste
Os resultados que  obteve mostram que o  modelo de Machine Learning está funcionando muito bem.

Desempenho Geral do Modelo
Acurácia: No conjunto de teste, o modelo alcançou uma acurácia de 86.38%, o que significa que ele classificou corretamente a maioria das imagens.

Perda (Loss): A perda de teste foi de 0.3726, indicando que o modelo cometeu poucos erros em suas previsões.

Área da Curva ROC (AUC): O valor de 0.9321 para o AUC é excelente. Um valor acima de 0.90 é considerado um desempenho ótimo para a maioria das tarefas de classificação. Isso significa que o modelo é muito bom em distinguir entre imagens normais e imagens com pneumonia.

Análise de Precisão e Recall
Para a classe NORMAL: O modelo teve uma precisão de 0.82 e um recall de 0.82. Isso significa que 82% das imagens classificadas como normais realmente eram, e o modelo detectou 82% de todas as imagens normais no conjunto de teste.

Para a classe PNEUMONIA: O modelo alcançou uma precisão de 0.89 e um recall de 0.89. Isso mostra que 89% das imagens classificadas como pneumonia eram realmente pneumonia, e o modelo detectou 89% de todos os casos de pneumonia.

Gráficos
Gráfico de Acurácia e Perda: O gráfico de acurácia mostra que a acurácia de validação cresce de forma consistente e é maior que a acurácia de treino, o que é um ótimo sinal. A curva de perda mostra que os erros de treino e validação diminuíram ao longo das 10 épocas.

Curva ROC: A curva ROC é um dos resultados mais importantes. A área abaixo da curva (AUC) é de 0.93, confirmando a alta capacidade do modelo de diferenciar as duas classes, com poucos falsos positivos e falsos negativos.

Matriz de Confusão
A matriz de confusão é uma representação visual do desempenho do seu modelo.

[[191 43]

[ 42 348]]

Verdadeiros Positivos (TP): 348 — O modelo acertou 348 vezes ao dizer que a imagem tinha pneumonia.

Verdadeiros Negativos (TN): 191 — O modelo acertou 191 vezes ao dizer que a imagem era normal.

Falsos Positivos (FP): 43 — O modelo errou 43 vezes ao dizer que uma imagem normal tinha pneumonia.

Falsos Negativos (FN): 42 — O modelo errou 42 vezes ao dizer que uma imagem com pneumonia era normal.

O número baixo de falsos negativos (42) é um resultado importante, pois significa que o modelo está minimizando o erro mais crítico em um diagnóstico médico: não detectar uma doença quando ela está presente.
