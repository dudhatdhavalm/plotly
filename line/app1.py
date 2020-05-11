import pandas as pd
import plotly.offline as offline
import plotly.graph_objs as graph

df = pd.read_csv("../data/nst-est2017-alldata.csv")
df_division_1 = df[df["DIVISION"] == '1']

df_division_1.set_index("NAME", inplace=True)

list_of_pop_col = [
    col for col in df_division_1.columns if col.startswith("POP")
]

df_division_1 = df_division_1[list_of_pop_col]

print(df_division_1.index)
data = [
    graph.Scatter(x=df_division_1.columns,
                  y=df_division_1.loc[name],
                  mode="lines",
                  name=name) for name in df_division_1.index
]

offline.plot(data)