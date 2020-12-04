import math

# Global Declarations
x=[]
y=[]
memo = []
for i in range(1 << 16):
    memo.append(-1.0)

linha, coluna = 20, 20
dist = [[0 for x in range(linha)] for y in range(coluna)] 
index1 = []
index2 = []
result = []
global N, target



def check(arr, n):
    for it in arr:
        if it == n:
            return True
    return False


def match(bitmask, target, N, memo, dist):
    global index1, index2, result
    if (memo[bitmask] > -0.5):
        return memo[bitmask]
    if(bitmask == target):
        memo[bitmask] = 0
        return 0
    ans = 20000000000.0
    for p1 in range(2*N):
        if(not(bitmask & (2**p1))):
            p1_state = p1
            break
    
    for p2 in range(p1_state + 1,2*N):
        if(not(bitmask & (2**p2))):
            ans = min(ans, dist[p1][p2] + match(bitmask | 2**p1 | 2 ** p2, target, N, memo, dist))
            index1.append(p1)
            index2.append(p2)
            result.append(ans)  
    
    memo[bitmask] = ans
    return ans
    
def main(x, y, pairs):
    global index1, index2, result
    #print(x, y)
    linha, coluna = 100, 100
    dist = [[0 for x in range(linha)] for y in range(coluna)] 
    N = pairs

    for i in range(2*N - 1):
        for j in range(i, 2*N):
            dist[i][j] = dist[j][i] = math.hypot(x[i] - x[j], y[i] - y[j])
        
    target = (1 << (2*N)) -1
    
    memo = []
    for i in range(1 << 16):
        memo.append(-1.0)

    print(match(0, target, N, memo, dist))
    arr = teams(index1, index2, result)
    #print("okay")
    return arr


def teams(index1, index2, result):
    save = []
    for i in range(30):
        save.append(-1)

    #print(index1)
    aux = 2000000000.0
    z = 0

    for i in range(len(index1)):       
        if(check(save, i) == True): continue
        for j in range(len(index1)):
            if (index1[j] == i or index2[j] == i):
                if(float(result[j]) < aux):
                    aux = result[j]
                    save[z] = index1[j]
                    save[z+1] = index2[j]            
        z+=2
        aux = 2000000000.0
    
    return save
