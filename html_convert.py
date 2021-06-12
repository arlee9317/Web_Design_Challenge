
import pandas as pd
from IPython.display import HTML

file = "Resources/cities.csv"
df = pd.read_csv(file)
df = df.set_index("City_ID")


result = df.to_html()
print(result)