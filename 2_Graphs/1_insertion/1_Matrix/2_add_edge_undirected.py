def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already presented in the Graph!!!!")
    else:
        node_count = node_count + 1
        nodes.append(v)

        for n in graph:
            n.append(0)

        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2):

    if v1 not in nodes:
        print(v1,"is not presented in Graph")
    elif v2 not in nodes:
        print(v2,"not presented in the Graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1

def print_graph():

    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()


nodes = []
graph = []
node_count = 0
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
print(graph)

add_edge("A","B")
add_edge("A",'C')
add_edge("A","D")
add_edge("B",'D')
add_edge("B","E")
add_edge("C","D")
add_edge("D","E")
print_graph()



