import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.plotting import autocorrelation_plot

from analise_de_vendas import plot_comparacao, plotar

alucel = pd.read_csv('arquivos/alucel.csv')
alucel.head()

alucel['dia'] = pd.to_datetime(alucel['dia'])
alucel.dtypes

print('Quantidade de linhas e colunas:', alucel.shape)
print('Quantidade de dados nulos:', alucel.isna().sum().sum())

alucel ['aumento'] = alucel ['vendas'].diff()
alucel ['aceleracao'] = alucel ['aumento'].diff()


#G1
plot_comparacao('dia', 'vendas', 'aumento', 'aceleracao', alucel, 'Análise de vendas da Alucel de Outubro e Novembro de 2018')


#Média Móvel
alucel['media_movel'] = alucel['vendas'].rolling(7).mean()
#G1
plotar('Análise de vendas com média móvel de 7 dias', 'Tempo', 'Média Móvel', 'dia', 'media_movel', alucel)

alucel['media_movel_21'] = alucel['vendas'].rolling(21).mean()

#G2
plotar('Análise de vendas com média móvel de 21 dias', 'Tempo', 'Média Móvel', 'dia', 'media_movel_21', alucel)

#G3
plot_comparacao('dia', 'vendas', 'media_movel', 'media_movel_21', alucel, 'Comparando as médias móveis')

