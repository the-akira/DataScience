import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('dados/2010YumaAZ.csv')

data = [go.Heatmap(x=df['DAY'],y=df['LST_TIME'], z=df['T_HR_AVG'].values.tolist())]

layout = go.Layout(title='Yuma')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='HTML/heatmaps_2.html') 