import re

def makednalist(string):
    l = string.split("\n")
    new = l[1:-1]
    data = []
    di = {}
    for x in new:
        data.append(x.replace(" -> ",",").split(","))
    for x in data:
        di[x[0]] = x[1:]
    return di
def find_degree(graph):
    deg = {}
    value = graph.values()
    key = graph.keys()
    for k in key:
        deg[k] = len(graph[k])
    for v in value:
        for i in range(len(v)):
            if v[i] not in deg:
                deg[v[i]] = 1
            else:
                deg[v[i]]+=1
    return deg
def find_odd(degree):
    return [k for k,v in degree.items() if v%2 != 0]
class Link:
    def __init__(self,node):
        self.node = node
        self.next = None
    def insert(self,link):
        link.next = self.next
        self.next = link
        return link
m = makednalist("""
0 -> 2
1 -> 3
2 -> 1
3 -> 0,4
6 -> 3,7
7 -> 8
8 -> 9
9 -> 6
""")
def eulerian_cycle(graph):
    graph = {k:v[:] for k,v in graph.items()}
    degree = find_degree(graph)
    newedge = find_odd(degree)
    if newedge[1] not in graph:
        graph[newedge[1]] = list(newedge[0])
        node = newedge[1]
    else:
        graph[newedge[0]].append(newedge[1])
        node = newedge[0]    
    choices  = graph[node]
    cur = Link(node)
    start = cur
    visited  = {}
    while True:
        cycle_start = node
        while choices:
            visited[node] = cur
            node = choices.pop()
            choices = graph[node]
            cur = cur.insert(Link(node))
        if node != cycle_start:
            raise ValueError("Graph has no Eulerian cycle")
        
        while visited:
            node,cur = visited.popitem()
            choices = graph[node]
            if choices:
                break
        else:
            break
    if any(graph.values()):
        raise ValueError("Graph has no Eulerian cycle")
    cycle = []
    cur = start
    while True:
        cycle.append(cur.node)
        cur = cur.next
        if cur == None:
            break
    return cycle[1:]
if __name__ == "__main__":
    v = eulerian_cycle(m)

    for x in v:
        print(x,end="->")
