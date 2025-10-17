#Objetivo do Projeto 🩻📒

Classificar imagens de raio-X em duas classes: NORMAL e PNEUMONIA, utilizando características extraídas do dataset (como intensidade média, desvio padrão, área máxima e perímetro máximo). O foco é treinar modelos de Machine Learning e analisar seu desempenho, incluindo os erros.

# Teste aplicado em um modelo ML clássico:
- Objetivo: Trazer os dados do arquivo CSV para dentro do Python e inspecionar.
- Usando a biblioteca Pandas, para ler as caracteristicas do CSV.
- Treinar e avaliar um modelo de classificação baseado em árvores (Random Forest).
- O modelo classifica as imagens em Pneumonia ou Normal e gera precisão.
- Treino usando SVM (Support Vector Machine)
- Análise dos erros
- 
# Resumo

O modelo é inadequado para uso clínico porque:

Ignora uma das classes (NORMAL) dependendo do ajuste.

Tem alta taxa de erro em predição de casos críticos.

Features simples não capturam a complexidade do problema.

Métricas superficiais (accuracy) mascaram falhas graves.
