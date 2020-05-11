import pandas as pd
import plotly.offline as offline
import plotly.graph_objs as graph

df = pd.read_csv("../data/mocksurvey.csv", index_col=0)

data = [
    graph.Bar(x=df[col], y=df.index, orientation="h", name="Question 1")
    for col in df.columns
]

layout = graph.Layout(title="Survey", barmode="stack")

fig = graph.Figure(data=data, layout=layout)

offline.plot(fig)
