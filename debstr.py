from collections import defaultdict

def de_bruijn(st,k):
    d = defaultdict(list)
    edges = []
    nodes = []
    for i in range(len(st)-k+1):
        if i < len(st)-k:
            edges.append((st[i:i+k],st[i+1:i+k+1]))
        nodes.append((st[i:i+k-1],st[i+1:i+k]))
    for k, v in nodes:
        d[k].append(v)
    m = list(d.items())
    for x in m:
        print(x[0],end=' -> ')
        my = ','.join(x[1])
        print(my)
    
