import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    FileData = list(reader)

FileData.pop(0)

NewData=[]

for i in range(len(FileData)):
	n_num = FileData[i][2]
	NewData.append(float(n_num))  

n = len(NewData)

total =0

for x in NewData:
    total += x

mean = total / n

print("Mean / Average is: " + str(mean))