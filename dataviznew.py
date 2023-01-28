import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

#Set working directory
os.chdir(r"C:\Users\User\Desktop\Ai Sg")

# Using csv module to read csv file
with open("sentiment.csv", "r") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    
# Use pandas to red csv
df = pd.read_csv("sentiment.csv")

# Extract the data for barchart
df = df.rename(columns=df.iloc[0])
y_values = df.iloc[0]

# Plot barchart
ax = y_values.plot.bar()
# Add x-axis labels
ax.set_xticklabels(header, rotation = 0)
# Add barchart labels
for i, v in enumerate(df.iloc[0]):
    ax.annotate(str(v), (i, v), xytext=(0, 10), textcoords='offset points', ha='center', verticalalignment='top')
# Add title
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

