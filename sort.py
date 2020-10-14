import random
data=[]
for i in range(0,10):
    data.append(random.randint(0,99))
print(data)

count=len(data)
for i in range(0,count):
    for j in range(0,count-i-1):
        if data[j]>data[j+1]:
            data[j],data[j+1]=data[j+1],data[j]
print(data)


