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
class Link:
    def __init__(self,node):
        self.node = node
        self.next = None
    def insert(self,link):
        link.next = self.next
        self.next = link
        return link
m = makednalist("""
0 -> 3
1 -> 0
2 -> 1,6
3 -> 2
4 -> 2
5 -> 4
6 -> 5,8
7 -> 9
8 -> 7
9 -> 6
""")
def eulerian_cycle(graph):
    graph = {k:v[:] for k,v in graph.items()}
    node = next(node for node,neighbour in graph.items() if neighbour)
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
    return cycle
if __name__ == "__main__":
    v = eulerian_cycle(m)

    for x in v:
        print(x,end="->")
