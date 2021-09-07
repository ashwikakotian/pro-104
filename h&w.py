import csv
from collections import Counter

with open ("h&w.csv",newline="")as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range(len (fileData)):
    num=fileData[i][1]
    newData.append(float(num))
n=len(newData)
total=0
for x in newData:
    total+=x


mean=total/n
print("Mean is : "+ str(mean))

newData.sort()
if n%2==0:
    median1=float(newData[n//2])
    median2=float(newData[n//2-1])
    median=(median1+median2)/2
else:
    median2=newData[n//2]
print("Median is : "+str(median))

data=Counter(newData)
modeDataforRange={"50-60":0,"60-70":0,"70-80":0}
for height ,occurance in data.items():
    if 50<float(height)<60:
        modeDataforRange["50-60"]+=occurance
    elif 60<float(height)<70:
        modeDataforRange["60-70"]+=occurance
    elif 70<float(height)<80:
        modeDataforRange["70-80"]+=occurance  
modeRange,modeoccurance=0,0    
for range ,o in modeDataforRange.items():
    if occurance>modeoccurance:
        modeRange, modeoccurance=[int(range.split("-")[0]),int((range.split("-")[1]))],occurance
mode=float((modeRange[0]+modeRange[1])/2)
print(f"Mode is -> {mode:2f}")

       


