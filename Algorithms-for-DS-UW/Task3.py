import sys
from collections import defaultdict

def tower_game(n, events):
    ret = [0 for _ in range(0,len(events))]
    tower = defaultdict(int)
    g_blocks = []
    
    max_height_temp = 0

    for i in range(0, n):
        
        score_temp = 0
        
        if events[i][1] == 1:
            tower[events[i][0]] += 1
            if tower[events[i][0]] not in g_blocks:
                g_blocks.append(tower[events[i][0]])
                score_temp += 1
                
        elif events[i][1] >= 4:
            tower[events[i][0]] = tower[events[i][0]] + events[i][1]
            if tower[events[i][0]] > max_height_temp:
                score_temp += 1
                max_height_temp = tower[events[i][0]]
     
        else:
            if events[i][1] == 2:
                max_in_hor = max(tower[events[i][0]], tower[events[i][0] + 1])
                tower[events[i][0]], tower[events[i][0]+1] = max_in_hor + 1, max_in_hor + 1
                if tower[events[i][0]] > max_height_temp:
                    score_temp += 1
                    max_height_temp = tower[events[i][0]]     
            else:
                max_in_hor = max(tower[events[i][0]], tower[events[i][0] + 1], tower[events[i][0] + 2])
                tower[events[i][0]], tower[events[i][0]+1], tower[events[i][0] + 2] = max_in_hor + 1, max_in_hor + 1, max_in_hor + 1
                if tower[events[i][0]] > max_height_temp:
                    score_temp += 1
                    max_height_temp = tower[events[i][0]]                   

        ret[i] = ret[i-1] + score_temp

    return ret
 

SUBMIT_TO_SZKOPUL = True
#SUBMIT_TO_SZKOPUL = False

if SUBMIT_TO_SZKOPUL:
    reader = sys.stdin
else:
    reader = inputReader = open("input0c.txt","r")
 
# Reads the input
astr = reader.readline().split()
n = int(astr[0])
events = [[int(val) for val in reader.readline().split()] for _ in range(0,n)]

# Calls your function
ret = tower_game(n, events)

# Writes the output
for i in range(0,n):
    print(ret[i])
    
