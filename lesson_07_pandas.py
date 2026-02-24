import pandas as pd

data = pd.read_csv("urban_data.csv")

print(data)

data["density"] = data["population"] / data["area"]

print(data)


