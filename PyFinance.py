import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import os
import subprocess

# Define o diretório onde você deseja salvar a imagem
output_directory = './generated_images'

# Cria o diretório se ele não existir
os.makedirs(output_directory, exist_ok=True)

df = yf.download('PETR4.SA',
                 start='2019-11-01',
                 end='2020-06-01',
                 group_by='ticker')

sns.set_theme(style="darkgrid")
sns.displot(df['Close'].dropna(), kde=True)

# Salva o gráfico como um arquivo de imagem
output_file = os.path.join(output_directory, 'grafico-1.png')
plt.savefig(output_file)

# Abre automaticamente a imagem usando o aplicativo padrão do sistema
#subprocess.Popen(['xdg-open', output_file])  # Para sistemas Linux
# subprocess.Popen(['open', output_file])     # Para sistemas macOS
subprocess.Popen(['start', output_file], shell=True)  # Para sistemas Windows

import yfinance as yf
import plotly.offline as py
import plotly.graph_objs as go

dados = [go.Scatter(x=df.index, y=df['Close'])]
layout = go.Layout(title='Histórico dos Preços da Ação',
                   yaxis={'title':'Preços'}, xaxis={'title': 'Período'})
fig = go.Figure(data=dados, layout=layout)

# Gere o arquivo HTML contendo o gráfico interativo
output_file = './generated_images/grafico-2.html'
py.plot(fig, filename=output_file, auto_open=False)

# Abre o arquivo HTML no navegador padrão do sistema
import webbrowser
webbrowser.open('file://' + os.path.abspath(output_file))


minimo=df['Close'].min()
print(f'minimo: {minimo}')

maximo=df['Close'].max()
print(f'maximo: {maximo}')

media=df['Close'].mean()
print(f'media: {media}')