import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

new=[]

for i in range(len(fileData)):
	n_num = fileData[i][1]
	new.append(n_num)

n = len(new)
new.sort()



if n % 2 == 0:

	median1 = float(new[n//2])

	median2 = float(new[n//2 - 1])

	median = (median1 + median2)/2
else:
	median = new[n//2]

print("Median is: " + str(median))