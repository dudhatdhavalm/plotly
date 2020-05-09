import numpy as np
import plotly.offline as offline
import plotly.graph_objs as graph

np.random.seed(56)

x_values = np.linspace(0,1,100)
y_values = np.random.random(100)

trace0 = graph.Scatter(
    x=x_values,
    y=y_values + 5,
    mode="markers",
    name="markers"
)

trace1 = graph.Scatter(
    x=x_values,
    y=y_values,
    mode="lines", 
    name="lines"
)

trace2 = graph.Scatter(
    x=x_values,
    y=y_values-5,
    mode="lines+markers", 
    name="lines+markers"
)

data = [trace0, trace1, trace2]

layout = graph.Layout(
    title="Line Chart"
)

fig = graph.Figure(data=data, layout=layout)

offline.plot(fig)