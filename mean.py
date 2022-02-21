import csv

with open("SOCR-HeightWeight.csv", newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

newData = []

for i in range(len(fileData)):
    n_num = fileData[i][1]
    newData.append(float(n_num))

n = len(newData)
total = 0

for x in newData:
    total += x

mean = total/n 

print("Mean/Average is: " + str(mean))