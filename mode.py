import csv
from collections import Counter

with open("SOCR-HeightWeight.csv", newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

newData = []

for i in range(len(fileData)):
    n_num = fileData[i][1]
    newData.append(float(n_num))

#Calculating mode
data = Counter(newData)
mode_date_for_range = {
                            "50-60": 0,
                            "60-70":0, 
                            "70-80":0
}

for height, occurence in data.items():
    if 50<float(height)<60:
        mode_date_for_range["50-60"]+= occurence
    elif 60<float(height)<70:
        mode_date_for_range["60-70"]+= occurence
    elif 70<float(height)<80:
        mode_date_for_range["70-80"]+= occurence

moderange, modeOccurence = 0, 0
for range, occurence in mode_date_for_range.items():
    if occurence > modeOccurence:
        moderange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((moderange[0]+ moderange[1])/2)

print(f"Mode is:{mode: 2f}")