import random
user=0
user_data=[0,0,0,0]
times=0
win_times=0
for i in range(0,10000):
    
    user=random.randint(0,2)
    user_data[user]+=1
    times+=1
    if user==3:
        break
    scissors=0.333
    rock=0.666
    computer=random.random()
    if user<0.4:
      user=0
    elif user<0.8:
      user=1
    else:
      user=2
    if computer<scissors:
        computer=0
    elif computer<rock: 
        computer=1
    else:
        computer=2
    
    if(user==0 and computer==2) or (user==1 and computer==0) or (user==2 and computer==1):
        win_times+=1

        #print('You win!')
    elif computer==user:
        a=1
        #print('Draw')
    else:
        a=1
        #print('You lose')
print('unoptmized:',win_times/10000)
