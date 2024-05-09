import sys


def best_influencer(n, m, s, links, inf_vals):
    
    ret = []
    
    INF = 1000000000
    delta = [ [INF] * n for v in range(n)]
    for [s,t,c] in links:
        delta[s][t] = min(delta[s][t], c)
    for v in range(n):
        delta[v][v] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                delta[i][j] = min(delta[i][j], delta[i][k] + delta[k][j])
      
    for i in delta:
        try:
            while True:
                i.remove(0)
        except:
            pass
    
    temp_1 = []
    for x in range(len(inf_vals)):
        temp = [] 
        for y in range(len(delta)):
            for z in delta[y]:
                if inf_vals[x][y] > z:
                    temp_1.append(inf_vals[x][y] - z)
                else:
                    temp_1.append(0)
            temp.append(sum(temp_1))
            temp_1 = []
            temp_indx = temp.index(max(temp))         
        ret.append(temp_indx)

    return ret
 

#SUBMIT_TO_SZKOPUL = False
SUBMIT_TO_SZKOPUL = True

if SUBMIT_TO_SZKOPUL:
    reader = sys.stdin
else:
    reader = inputReader = open("input0a.txt","r")
 
# Reads the input
astr = reader.readline().split()
n=int(astr[0])
m=int(astr[1])
s=int(astr[2])
reader.readline()
links = [[int(val) for val in reader.readline().split()] for _ in range(m)]
reader.readline()
inf_vals = [[int(val) for val in reader.readline().split()] for _ in range(s)]

# Calls your function
ret = best_influencer(n, m, s, links, inf_vals)

# Writes the output
for i in range(s):
    print(ret[i])
    
