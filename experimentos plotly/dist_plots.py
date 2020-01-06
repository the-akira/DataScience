import plotly.offline as pyo 
import plotly.figure_factory as ff 
import numpy as np 

x1 = np.random.randn(200)-3
x2 = np.random.randn(200)
x3 = np.random.randn(200)+3
x4 = np.random.randn(200)+4

hist_data = [x1,x2,x3,x4]
group_labels = ['x1','x2','x3','x4']

fig = ff.create_distplot(hist_data, group_labels, bin_size=[.2,.1,.3,.4])

pyo.plot(fig, filename='dist_plots.html') 