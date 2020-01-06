import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('mpg.csv')

data = [go.Histogram(x=df['mpg'], xbins=dict(start=0,end=50,size=2))]

layout = go.Layout(title='Histogram')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='histogram.html')