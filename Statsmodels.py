import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.plotting import autocorrelation_plot
from analise_de_vendas import plotar, plot_comparacao
from statsmodels.tsa.seasonal import seasonal_decompose

resultado = seasonal_decompose("arquivos/chocolura['vendas']", freq=1)
ax = resultado.plot()

observacao = resultado.observed
tendencia = resultado.trend
sazonalidade = resultado.seasonal
ruido = resultado.resid

data = ({
       'observacao':observacao,
       'tendencia':tendencia,
       'sazonalidade':sazonalidade,
       'ruido':ruido
})
resultado = pd.DataFrame(data)
resultado.head


#G1
plot_comparacao(resultado.index, 'observacao', 'tendencia', 'sazonalidade', resultado, 'Exemplo de Statsmodels')

#G2
plot_comparacao(resultado.index, 'observacao', 'tendencia', 'ruido', resultado, 'Exemplo de Statsmodels')

