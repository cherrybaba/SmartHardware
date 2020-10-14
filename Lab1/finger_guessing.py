import random
user=0
user_data=[0,0,0,0]
times=0
while True:
    user_raw=input('Please input scissors(0) rock(1) paper(2) quit(3):')
    while not user_raw.isdigit() or int(user_raw)>3:
        user_raw=input('Please input a number ranged in 0-3: ')
    user=int(user_raw)
    user_data[user]+=1
    times+=1
    if user==3:
        break
    scissors=user_data[0]/times
    rock=scissors+user_data[1]/times
    computer=random.random()
    if computer<scissors:
        computer=1
    elif computer<rock: 
        computer=2
    else:
        computer=0
    
    if(user==0 and computer==2) or (user==1 and computer==0) or (user==2 and computer==1):
        print('You win!')
    elif computer==user:
        print('Draw')
    else:
        print('You lose')

