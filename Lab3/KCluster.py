import numpy as np
import matplotlib.pyplot as plt
import random
import time

User1Mean=28
User1Sigma=1
User2Mean=24
User2Sigma=1.3

dataNum=random.randint(0,2160)
user1TempData=User1Mean+User1Sigma*np.random.randn(dataNum)
user2TempData=User2Mean+User2Sigma*np.random.randn(2160-dataNum)
userData=np.append(user1TempData,user2TempData)
plt.hist(userData,216,histtype='bar',facecolor='yellowgreen',alpha=0.75)
plt.show()
user1=user1TempData[0]
user2=user2TempData[0]
user1Last=-1
user2Last=50
while abs(user1-user1Last)!=0 or abs(user2-user2Last)!=0:
  user1Last=user1
  user2Last=user2
  user1Num=0
  user2Num=0
  user1=user2=0
  for t in userData:
    if abs(user1Last-t)<abs(user2Last-t):
      user1Num+=1
      user1+=t
    else:
      user2Num+=1
      user2+=t
  user1/=user1Num
  user2/=user2Num

print("User1's favorite temperature maybe {:.2f}, his office time maybe {:.2f} hours per month.".format(user1,user1Num/6))
print("User2's favorite temperature maybe {:.2f}, his office time maybe {:.2f} hours per month.".format(user2,user2Num/6))
'''
f=open('/sys/bus/w1/devices/28-0000096579d5/w1_slave','r')
lines=f.readlines()
t=0
if lines[0][-4:-1]=='YES':
  pos=lines[1].find('t=')
  t=int(lines[1][pos+2:])/1000
  print("Current temperature is {:.2f}.".format(t))
  if abs(t-user1)<abs(t-user2):
    print('Current user maybe user1.')
  else:
    print('Current user maybe user2.')
    '''
plt.show()

















