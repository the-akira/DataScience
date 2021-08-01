import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 
import numpy as np 

df = pd.read_csv('dados/abalone.csv')

a = np.random.choice(df['rings'],30,replace=False)
b = np.random.choice(df['rings'],20,replace=False)

data = [go.Box(y=a,name='A'), go.Box(y=b, name='B')]
layout = go.Layout(title='2 random samples')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='HTML/box_plots_exercicios.html')