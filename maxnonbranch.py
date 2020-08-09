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
    outdeg = {}
    value = graph.values()
    key = graph.keys()
    for k in key:
        deg[k] = len(graph[k])
        outdeg[k] = len(graph[k])
    for v in value:
        for i in range(len(v)):
            if v[i] not in deg:
                deg[v[i]] = 1
                outdeg[v[i]] = 0
            else:
                deg[v[i]]+=1
    indeg = {key: deg[key] - outdeg.get(key, 0) for key in deg}
    
    return deg,indeg,outdeg

def isolated_cycle(graph):
    key = list(graph.keys())
    key.append('None')
    start = key[0]
    isolated = []
    _,indeg,outdeg = find_degree(graph)
    while start != 'None':
        node = start
        li = []
        while (indeg[node] == 1 and outdeg[node] == 1):
            li.append(node)
            key.remove(node)
            node = graph[node][0]
            if node == start:
                li.append(node)
                isolated.append(li)
                start = key[0]
                break
    return isolated                
def max_nonbranching(graph):
    newgraph = makednalist(graph)
    paths = []
    node,indeg,outdeg = find_degree(newgraph)
    
    for key in node.keys():
        if not (indeg[key] == 1 and outdeg[key] == 1):
            if outdeg[key] > 0:
                for outedge in newgraph[key]:
                    nonbranch = []
                    nonbranch.append(key)
                    nonbranch.append(outedge)
                    while indeg[outedge] == 1 and outdeg[outedge] == 1:
                        nonbranch.extend(newgraph[outedge])
                        p = newgraph[outedge]
                        outedge = p[0]
                    paths.append(nonbranch) 
    new2 = makednalist(graph)
    for elem in paths:
        for i in range(len(elem)):
            if elem[i] in new2:
                del new2[elem[i]]
    
    isolated = isolated_cycle(new2)
    for x in isolated:
        paths.append(x)
    return paths
            
