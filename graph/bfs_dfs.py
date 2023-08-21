def dfs(graph, node, visited = set()):
    print(node,end = '\t')
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph , child , visited)


def bfs(graph,start):
    visited = set()
    queue = [start]
    front = 0
    
    while front < len(queue):
        node = queue[front]
        front +=1

        if node not in visited:
            print(node,end = '\t')
            visited.add(node)
            queue.extend(i for i in graph[node] if i not in visited)

n = 6
conn = [[0,1],[0,2],[0,3],[0,4],[1,3],[2,3],[2,5],[3,5]]


graph_dict = {}
for i in range(6):
    graph_dict[i] = []

for (u,v) in  conn:
    graph_dict[u].append(v)
    graph_dict[v].append(u)

for j in graph_dict:
    print(j,graph_dict[j])

dfs(graph_dict , 3)
bfs(graph_dict , 3)