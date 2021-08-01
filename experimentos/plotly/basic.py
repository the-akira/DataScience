import numpy as np 
import plotly.offline as pyo 
import plotly.graph_objs as go 

np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x=random_x, y=random_y, mode='markers', marker=dict(size=12, color='rgb(51,204,123)'))]
layout = go.Layout(title='Primeiro Título', xaxis={'title':'eixo x'}, yaxis=dict(title='meu eixo y'), hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='HTML/scatter.html')