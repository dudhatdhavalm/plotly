import plotly.graph_objs as graph
import plotly.offline as offline
import pandas as pd

df = pd.read_csv("../data/2018WinterOlympics.csv")
trace1 = graph.Bar(x=df["NOC"],
                   y=df["Gold"],
                   name="Gold",
                   marker={"color": "#FFD700"})

trace2 = graph.Bar(x=df["NOC"],
                   y=df["Silver"],
                   name="Silver",
                   marker={"color": "#9EA0A1"})

trace3 = graph.Bar(x=df["NOC"],
                   y=df["Bronze"],
                   name="Bronze",
                   marker={"color": "#CD7F32"})

data = [trace1, trace2, trace3]

#layout = graph.Layout(title="Medals")
layout = graph.Layout(title="Medals", barmode="stack")

fig = graph.Figure(data=data, layout=layout)

offline.plot(fig)
