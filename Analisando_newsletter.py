#Analisando assinantes da newsletter

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.plotting import autocorrelation_plot

from analise_de_vendas import plot_comparacao

assinantes = pd.read_csv('arquivos/newsletter_alucar.csv')
assinantes.head()

assinantes.dtypes


print('Quantidade de linhas e colunas', assinantes.shape)
print('Quantidade de dados nulos', assinantes.isna().sum().sum())


assinantes['mes'] = pd.to_datetime(assinantes['mes'])
assinantes.dtypes


assinantes['aumento'] = assinantes ['assinantes'].diff()
assinantes['aceleracao'] = assinantes ['aumento'].diff()
assinantes.head()


plot_comparacao('mes', 'assinantes', 'aumento', 'aceleracao',
                assinantes, 'Análise de assinantes da newsletter')


