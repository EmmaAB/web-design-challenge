import pandas as pd
import os

cities = os.path.join("Resources/cities.csv")
cities_df = pd.read_csv(cities)

cities_df.to_html("data.html", index=False)

data_table = cities_df.to_html()
print(data_table)

