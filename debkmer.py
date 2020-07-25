from collections import defaultdict

def makednalist(string):
    l = string.split("\n")
    return l[1:-1]

def de_bruijn(string):
    d = defaultdict(list)
    edges = makednalist(string)
    l = len(edges[0])
    nodes = []
    for i in edges:
        nodes.append((i[0:l-1],i[1:]))
    for k, v in nodes:
        d[k].append(v)
    m = list(d.items())
    for x in m:
        print(x[0],end=' -> ')
        my = ','.join(x[1])
        print(my)
    
