##Car - Analisando as vendas

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.plotting import autocorrelation_plot


#bloco1
alucar = pd.read_csv('arquivos/alucar.csv').head()
print(f'Quantidade de linhas e colunas {alucar.shape}')
alucar.head(10)
print(f'Quantidade de dados nulos {alucar.isna().sum().sum()}')
alucar.dtypes
alucar['mes'] = pd.to_datetime(alucar['mes'])

#Gráfico1
sns.lineplot(x='mes', y='vendas', data=alucar)

#Gráfico2
sns.set_palette('Accent')
sns.set_style('darkgrid')
ax = sns.lineplot(x='mes', y='vendas', data=alucar)
ax.figure.set_size_inches(12,6)
ax.set_title('Vendas alucar de 2017 e 2018', loc='left', fontsize=18)
ax.set_xlabel('Tempo', fontsize=14)
ax.set_ylabel('Vendas (R$)', fontsize=14)


#Bloco2
alucar['aumento'] = alucar[['vendas']].diff()
alucar.head(8)


#Gráfico3
sns.set_palette('Accent')
sns.set_style('darkgrid')
ax = sns.lineplot(x='mes', y='aumento', data=alucar)
ax.figure.set_size_inches(12,6)
ax.set_title('Aumento das vendas Car de 2017 e 2018', loc='left', fontsize=18)
ax.set_xlabel('Tempo', fontsize=14)
ax.set_ylabel('Aumento', fontsize=14)


#Bloco3
def plotar(titulo, labelx, labely, x, y, dataset):
    sns.set_palette('Accent')
    sns.set_style('darkgrid')
    ax = sns.lineplot(x=x, y=y, data=dataset)
    ax.figure.set_size_inches(12,6)
    ax.set_title(titulo, loc='left', fontsize=18)
    ax.set_xlabel(labelx, fontsize=14)
    ax.set_ylabel(labely, fontsize=14)


#Gráfico4
plotar('Aumento das vendas Car de 2017 e 2018', 'Tempo', 'Aumento', 'mes', 'aumento', alucar)

#Gráfico5
alucar['aceleracao'] = alucar['aumento'].diff()
plotar ('Aceleração das vendas da alucar de 2017 e 2018', 'Tempo', 'Aceleração', 'mes','aceleracao', alucar)


#Gráfico6
plt.figure(figsize=(16,12))
ax = plt.subplot(3,1,1)
ax.set_title('Análise das vendas da Alucar 2017 e 2018',fontsize=18, loc='left')
sns.lineplot(x='mes', y='vendas', data=alucar)
plt.subplot(3,1,2)
sns.lineplot(x='mes', y='aumento', data=alucar)
plt.subplot(3,1,3)
sns.lineplot(x='mes', y='aceleracao', data=alucar)
ax=ax


#Bloco4
def plot_comparacao(x, y1, y2, y3, dataset, titulo):
    plt.figure(figsize=(16,12))
    ax = plt.subplot(3,1,1)
    ax.set_title(titulo,fontsize=18, loc='left')
    sns.lineplot(x=x, y=y1, data=dataset)
    plt.subplot(3,1,2)
    sns.lineplot(x=x, y=y2, data=dataset)
    plt.subplot(3,1,3)
    sns.lineplot(x=x, y=y3, data=dataset)
    ax=ax



#Gráfico7
plot_comparacao('mes', 'vendas', 'aumento', 'aceleracao',
                alucar, 'Análise das vendas da alucar de 2017 e 2018')



#Gráfico8
ax = plt.figure(figsize=(12,6))
autocorrelation_plot(alucar['vendas'])
ax = ax


#Gráfico9
ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação das Vendas', fontsize=18, x=0.26, y= 0.95)
autocorrelation_plot(alucar['vendas'])
ax=ax



#Gráfico10
ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação do aumento', fontsize=18, x=0.26, y= 0.95)
autocorrelation_plot(alucar['aumento'][1:])
ax=ax



#Gráfico11
ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação da aceleraçao', fontsize=18, x=0.26, y= 0.95)
autocorrelation_plot(alucar['aceleracao'][2:])
ax=ax