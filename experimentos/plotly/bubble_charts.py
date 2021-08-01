import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('dados/mpg.csv')
print(df)
print(df.columns)

data = [go.Scatter(x=df['horsepower'],y=df['mpg'],text=df['name'], mode='markers', marker=dict(size=2*df['cylinders'], color=df['cylinders'], showscale=True))]

layout = go.Layout(title='Bubble Chart')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='HTML/bubble_charts.html')