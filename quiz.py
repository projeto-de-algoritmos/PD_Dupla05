import math



x=[]
y=[]
memo = []
linha, coluna = 20, 20
dist = [[0 for x in range(linha)] for y in range(coluna)] 
pos = [[0 for x in range(linha)] for y in range(2)]
for i in range(1 << 16):
    memo.append(-1.0)

def match(bitmask):
    global k, N, target, memo, dist
    if (memo[bitmask] > -0.5):
        return memo[bitmask]
    if(bitmask == target):
        memo[bitmask] = 0
        return 0
    ans = 20000000000.0
    for p1 in range(2*N):
        #print(p1)
        if(not(bitmask & (2**p1))):
            p1_state = p1
            break
    #prev = min(ans, dist[p1+1][p1+1] + match(bitmask | 2**p1 | 2 ** (p1 +1)))
    
    for p2 in range(p1_state + 1,2*N):
        if(not(bitmask & (2**p2))):
            ans = min(ans, dist[p1][p2] + match(bitmask | 2**p1 | 2 ** p2))
            print(p1, p2, ans)
            
    #pos[0][]x,y)
    
    memo[bitmask] = ans
    return ans
    

N = int(input())

for i in range(2*N):
    inp = input().split()      
    x.append(int(inp[1]))
    y.append(int(inp[2]))


for i in range(2*N - 1):
    for j in range(i, 2*N):
        dist[i][j] = dist[j][i] = math.hypot(x[i] - x[j], y[i] - y[j])
        

target = (1 << (2*N)) -1

print(match(0))

"""
elements = set()

for i in range(linha):
    for j in range(coluna):
        elements.add(dist[i][j])

#print(elements)

for i in range(1, 10):  
    print(dist[0])
    print (dist[i])
"""


