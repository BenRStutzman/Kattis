import sys

def search_from(node, graph, checked, stuck, bugs):
    #print("node:", node)
    #print("graph", graph)
    #print("checked:", checked)
    #print("stuck:", stuck)
    #print("bugs:", bugs)
    #print("checked[0]", checked[0])
    #print("checked[1]", checked[1])
    if (node in checked[0]) or (node in checked[1] and bugs):
        return stuck, checked
    checked[bugs].add(node)
    
    if graph[node][0]:
        stuck, checked = search_from(graph[node][0], graph, checked, stuck, bugs)
    else:
        stuck.add(node)
    if not bugs:
        for next_node in graph[node][1]:
            stuck, checked = search_from(next_node, graph, checked, stuck, 1)
    
    #print(stuck, checked)
    return stuck, checked
    
def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N, E = inp[0]
    
    graph = [[0, []] for i in range(N + 1)]
    graph[0] = [1, []]
    
    for a, b in inp[1:E + 1]:
        if a < 0:
            graph[-a][0] = b
        else:
            graph[a][1].append(b)
            
    #print(search_from(0, graph, [set(), set()], set(), 0))
    
    print(len(search_from(0, graph, [set(), set()], set(), 0)[0]))
    
main()
