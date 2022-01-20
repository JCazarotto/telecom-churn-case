import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px


tabela = pd.read_csv(r'C:\Users\jcazarotto\Desktop\Phyton\Aula 02\telecom_users.csv')

'''parametro axis é 1 para coluna e 0 para linha, deletando a coluna Unnamed: 0'''
tabela = tabela.drop('Unnamed: 0', axis=1)

'''transformar o tipo de dados da coluna TotalGasto de 'object' (texto) para 'float' (numero decimal)
o parametro errors='coerce' apaga os dados com erro'''
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

'''excluir colunas com valores vazios, o parametro how estipula quantos valores vazios a coluna deve ter para ser 
excluida how='all' são colunas completamente vazias e how='any' são colunas com algum valor vazio'''
tabela = tabela.dropna(how='all', axis=1)

'''excluir linhas com valores vazios, o parametro how estipula quantos valores vaxios a linha deve ter para ser excluida
how='all' são linhas completamente vazias e how='any' são linhas com algum valor vazio'''
tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())
'''Contagem dos valores da coluna Churn e contagem normalizada e editada em %'''
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map("{:.2%}".format))
'''#grafico plotado com o matplotlib
grafico = tabela['Churn'].value_counts(normalize=True)*100
x = ['Nao', 'Sim']
plt.bar(x, height=grafico)
plt.title('Total Cancelamentos (%)')
plt.xticks(x)
plt.yticks(grafico)
plt.xlabel('Cancelamentos')
plt.ylabel('Contagem')
plt.show()
'''
# grafico plotado com o plotly
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()
