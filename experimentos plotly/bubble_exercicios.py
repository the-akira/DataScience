import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('mpg.csv')

data = [go.Scatter(x=df['displacement'], y=df['acceleration'], text=df['name'], mode='markers', marker=dict(size=df['weight']/400))]

layout = go.Layout(title='My Bubble Solution', hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='bubble_exercicios.html')