import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.plotting import autocorrelation_plot

from analise_de_vendas import plot_comparacao

chocolura = pd.read_csv('arquivos/chocolura.csv')
chocolura.head()

chocolura.dtypes

chocolura['mes'] = pd.to_datetime(chocolura['mes'])
chocolura.dtypes


print('Quantidade de linhas e colunas', chocolura.shape)
print('Quantidade de dados nulos', chocolura.isna().sum().sum())


chocolura['aumento']= chocolura ['vendas'].diff()
chocolura['aceleracao']= chocolura ['aumento'].diff()


plot_comparacao('mes', 'vendas', 'aumento', 'aceleracao', chocolura, 'Análise de vendas da Chocolura de 2017 a 2018')

