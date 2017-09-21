import time
import os

# write the acronym of my name as follows
a_1="#         ######    #       #"
a_2="#         #     #    #     #"
a_3="#         #      #    #   #"
a_4="#         #       #    # #"
a_5="#         #       #     #"
a_6="#         #       #    # # "
a_7="#         #      #    #   #"
a_8="#         #     #    #     #"
a_9="########  ######    #       #"

space=' '

for i in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
    # each loop will move the strings to the right by 1 step
    
    t=os.system('cls')
    # use cls to clean the screen before printing the result each time
    
    # the following loop uses commands in the formated strings to print the result
    for j in (1,2,3,4,5,6,7,8,9):
        exec('b_%d=space+a_%d'%(j,j))
        exec('print(b_%d)'%(j))
    space=space+' '
    
    time.sleep(0.2)
    # pause for 0.2 second so that we can see the movement