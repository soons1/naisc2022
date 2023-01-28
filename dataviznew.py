import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

os.chdir(r"C:\Users\User\Desktop\Ai Sg")

with open("sentiment.csv", "r") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)

df = pd.read_csv("sentiment.csv")
df = df.rename(columns=df.iloc[0])
y_values = df.iloc[0]

ax = y_values.plot.bar()
ax.set_xticklabels(header, rotation = 0)

for i, v in enumerate(df.iloc[0]):
    ax.annotate(str(v), (i, v), xytext=(0, 10), textcoords='offset points', ha='center', verticalalignment='top')

plt.title("Distribution of satisfaction levels")
plt.show()

# import csv
# import os
# import pandas as pd
# import plotly.graph_objs as go
# import matplotlib.pyplot as plt

# os.chdir(r'C:\Users\User\Desktop')

# df = pd.read_csv("sentiment.csv")
# data = df.iloc[:,1]

# with open("sentiment.csv", "r") as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     #print(header)

#     for row in csvreader:
#         num = row
#     #print(row)

# bar_chart = go.Figure(data=[go.Bar(x=header, y=data)])
# bar_chart.show()

