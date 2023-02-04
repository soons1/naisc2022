import csv
import os
import senticGCNBERT

# To be set by the user
os.chdir(r'C:\Users\User\Desktop')

list_output = senticGCNBERT.output

neutral = 0
negative = 0
positive = 0

# Counting the number of -1/0/1
for dict in list_output:
    labels_lst = dict["labels"]
    for num in labels_lst:
        if num == 0:
            neutral += 1
        elif num < 0:
            negative += 1
        else:
            positive += 1
            
# Set the header for the csv file
header = ["Negative", "Neutral", "Positive"]
data = [negative, neutral, positive]

# Writing the csv file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerow(data)
    
