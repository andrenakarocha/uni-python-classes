import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv("/home/andrenakarocha/Downloads/dado_mg.csv")
coluna_original = dados.columns[0]
colunas = dados.columns[0].split(';')
dado = dados[coluna_original][0].split(";")

dic = {}

for i in range(len(dado)):
    dic[colunas[i]] = [dado[i]]

for i in range(len(dados)):
    dado = dados[coluna_original][i].split(";")
    for j,key in enumerate(dic.keys()):
        elem = dado[j]
        dic[key].append(elem)

dados = pd.DataFrame(dic)

histograma = []
for i in range(len(dados['SG_UF_RESIDENCIA'].unique())):
    residencias = dados['SG_UF_RESIDENCIA']
    histograma.append([residencias.unique()[i], residencias.value_counts()[i]])
histograma = pd.DataFrame(histograma)

plt.bar(histograma[:][0], histograma[:][1])
plt.yscale('log')
plt.grid()
plt.title('Quantidade de candidatos por estado', fontsize=25)
plt.figure()

compareceram = dados[dados['NU_NOTA_REDACAO'] != '']
nao_compareceram = dados[dados['NU_NOTA_REDACAO'] == '']

labels = ["F","M"]
plt.title("Presentes por Gênero")
plt.pie([compareceram['TP_SEXO'].value_counts()[0],compareceram['TP_SEXO'].value_counts()[1]],labels = labels)
plt.figure()

labels = ['Pública', 'Privada']
plt.title('Presentes por tipo de escola')
plt.pie([compareceram['TP_ESCOLA'].value_counts()[0], compareceram['TP_ESCOLA'].value_counts()[1]], labels = labels)
plt.figure()
plt.title('Ausentes por tipo de escola')
plt.pie([nao_compareceram['TP_ESCOLA'].value_counts()[0], nao_compareceram['TP_ESCOLA'].value_counts()[1]], labels = labels)
plt.figure()
plt.show()

dict_pesos = {
    'NU_NOTA_CN': 1,
    'NU_NOTA_CH': 3,
    'NU_NOTA_MT': 1,
    'NU_NOTA_REDACAO': 3,
    'NU_NOTA_LC': 2
}


