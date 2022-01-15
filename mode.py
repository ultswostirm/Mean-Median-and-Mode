import csv
from collections import Counter

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(float(n_num))

n = len(new_data)
data=Counter(new_data)
mode_range={
"50-60":0, "60-70":0, "70-80":0
}
for height, occurence in data.items():
    if 50<float(height)<60:
        mode_range["50-60"]+=occurence
    elif 60<float(height)<70:
        mode_range["60-70"]+=occurence
    elif 70<float(height)<80:
        mode_range["70-80"]+=occurence
        
modeRange,modeOccurence=0,0
for range,occurence in mode_range.items():
    if occurence>modeOccurence:
        modeRange,modeOccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode=float((modeRange[0]+modeRange[1])/2)

print(f"Mode is -> {mode:2f}")