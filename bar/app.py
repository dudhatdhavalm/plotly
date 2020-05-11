import plotly.graph_objs as graph
import plotly.offline as offline
import pandas as pd

df = pd.read_csv("../data/2018WinterOlympics.csv")

data = [graph.Bar(x=df["NOC"], y=df["Total"])]

layout = graph.Layout(title="Medals")

fig = graph.Figure(data=data, layout=layout)

offline.plot(fig)
