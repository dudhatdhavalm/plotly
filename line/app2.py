import pandas as pd
import plotly.graph_objs as graph
import plotly.offline as offline

df = pd.read_csv("../data/2010YumaAZ.csv")
print(df)
days = [
    "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY",
    "MONDAY"
]

data = []
for day in days:
    day_df = df[df["DAY"] == day]
    trace = graph.Scatter(x=day_df["LST_TIME"],
                          y=day_df["T_HR_AVG"],
                          mode="lines",
                          name=day)
    data.append(trace)

layout = graph.Layout(title="Remperature Data")

fig = graph.Figure(data=data, layout=layout)

offline.plot(fig)
