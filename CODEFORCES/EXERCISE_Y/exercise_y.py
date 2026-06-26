import sys  
input = sys.stdin.readline
resultados = []
def solve():  
    n, k= map(int, input().split())
    s = input().strip()

    grupos = {}
    for i in range(n):
        g = i % k 
        grupos[g] = grupos.get(g, 0) + int(s[i])
    
    for cnt in grupos.values():
        if cnt % 2 != 0:
            resultados.append("NO")
            return
    resultados.append("YES")

t = int(input())
for _ in range(t):
    solve()

for res in resultados:
    print(res)