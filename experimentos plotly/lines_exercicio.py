import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 

df = pd.read_csv('2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

data = []

for day in days:
	trace = go.Scatter(x=df['LST_TIME'],y=df[df['DAY']==day]['T_HR_AVG'],mode='lines',name=day)
	data.append(trace)

# Define o layout
layout = go.Layout(title='Temperaturas médias diárias')

# Cria uma figura através dos dados e layout
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='lines_exercicio.html')