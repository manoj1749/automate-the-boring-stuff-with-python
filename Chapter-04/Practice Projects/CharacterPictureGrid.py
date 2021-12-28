import random
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinOutput = []
    for i in range(100):
        h = random.randint(0,1)
        if h==0:
            coinOutput.append('H')
        elif h ==1:
            coinOutput.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    coinStreak = 0    
    for i in range(100):
        if coinOutput[i:i+6]==['H','H','H','H','H','H'] or coinOutput[i:i+6]==['T', 'T', 'T', 'T', 'T', 'T']:
            coinStreak+=1
        if coinStreak==6:
            numberOfStreaks+=1
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))