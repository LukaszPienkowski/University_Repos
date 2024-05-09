import sys
import bisect
import math

def adv_effect(m, c, u, regist_times, start_times, durations):
    regist_times.sort()
    ret = [-1 for _ in range(0,c)]
    end_times = [sum(x) - 1 for x in zip(start_times, durations)]
    start_pos = [bisect.bisect_left(regist_times, i) for i in start_times]
    end_pos = [bisect.bisect_right(regist_times, i) - 1 for i in end_times]

    for i in range(0,len(start_pos)):
        if start_pos[i] == end_pos[i] and start_pos[i] == len(regist_times) - 1:
            ret[i] = regist_times[end_pos[i]] - start_times[i] 
        else: 
            if end_times[i]+1-start_times[i] == 0 or end_pos[i]-start_pos[i] < 0: 
                ret[i] = 0   
            else:
                ret[i] = regist_times[math.floor((end_pos[i]+start_pos[i])/2)] - start_times[i] 
    return ret

SUBMIT_TO_SZKOPUL = True
#SUBMIT_TO_SZKOPUL = False

if SUBMIT_TO_SZKOPUL:
    reader = sys.stdin
else:
    reader = inputReader = open("input0b.txt","r")
 
# Reads the input
astr = reader.readline().split()
m=int(astr[0])
u=int(astr[1])
c=int(astr[2])
# Read join dates
regist_times = [-1 for _ in range(u)] 
astr = reader.readline().split()
for i in range(u):
    regist_times[i] = int(astr[i])
# Read campaign start dates
start_times = [-1 for _ in range(c)] 
astr = reader.readline().split()
for i in range(c):
    start_times[i] = int(astr[i])
# Read campaign durations
durations = [-1 for _ in range(c)] 
astr = reader.readline().split()
for i in range(c):
    durations[i] = int(astr[i])

# Calls your function
ret = adv_effect(m, c, u, regist_times, start_times, durations)

# Writes the output
for i in range(0,c):
    print(ret[i])
