##Car - Analisando as vendas

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.plotting import autocorrelation_plot


#bloco1
car = pd.read_csv('arquivos\car.csv').head()
print(f'Quantidade de linhas e colunas {car.shape}')
car.head(10)
print(f'Quantidade de dados nulos {car.isna().sum().sum()}')
car.dtypes
car['mes'] = pd.to_datetime(car['mes'])

#Gráfico1
sns.lineplot(x='mes', y='vendas', data=car)

#Gráfico2
sns.set_palette('Accent')
sns.set_style('darkgrid')
ax = sns.lineplot(x='mes', y='vendas', data=car)
ax.figure.set_size_inches(12,6)
ax.set_title('Vendas Car de 2017 e 2018', loc='left', fontsize=18)
ax.set_xlabel('Tempo', fontsize=14)
ax.set_ylabel('Vendas (R$)', fontsize=14)


#Bloco2
car['aumento'] = car[['vendas']].diff()
car.head(8)


#Gráfico3
sns.set_palette('Accent')
sns.set_style('darkgrid')
ax = sns.lineplot(x='mes', y='aumento', data=car)
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
plotar('Aumento das vendas Car de 2017 e 2018', 'Tempo', 'Aumento', 'mes', 'aumento', car)

#Gráfico5
car['aceleracao'] = car['aumento'].diff()
plotar ('Aceleração das vendas da Car de 2017 e 2018', 'Tempo', 'Aceleração', 'mes','aceleracao', car)


#Gráfico6
plt.figure(figsize=(16,12))
ax = plt.subplot(3,1,1)
ax.set_title('Análise das vendas da Alucar 2017 e 2018',fontsize=18, loc='left')
sns.lineplot(x='mes', y='vendas', data=car)
plt.subplot(3,1,2)
sns.lineplot(x='mes', y='aumento', data=car)
plt.subplot(3,1,3)
sns.lineplot(x='mes', y='aceleracao', data=car)
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
                car, 'Análise das vendas da Car de 2017 e 2018')



#Gráfico8
ax = plt.figure(figsize=(12,6))
autocorrelation_plot(car['vendas'])
ax = ax


#Gráfico9
ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação das Vendas', fontsize=18, x=0.26, y= 0.95)
autocorrelation_plot(car['vendas'])
ax=ax



#Gráfico10
ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação do aumento', fontsize=18, x=0.26, y= 0.95)
autocorrelation_plot(car['aumento'][1:])
ax=ax



#Gráfico11
ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação da aceleraçao', fontsize=18, x=0.26, y= 0.95)
autocorrelation_plot(car['aceleracao'][2:])
ax=ax