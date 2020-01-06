import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('2010SantaBarbaraCA.csv')

data = [go.Heatmap(x=df['DAY'],y=df['LST_TIME'], z=df['T_HR_AVG'].values.tolist())]

layout = go.Layout(title='SB CA Temps')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmaps.html') 