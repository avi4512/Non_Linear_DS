def add_node(v):
    global n_count
    if v in nodes:
        print(v,'is Already Present in the Graph')
    else:
        n_count = n_count + 1
        nodes.append(v)

        for i in graph:
            i.append(0)

        list1 = []
        for j in range(n_count):
            list1.append(0)
        graph.append(list1)

def show():
    for i in range(n_count):
        for j in range(n_count):
            print(graph[i][j],end=" ")
        print()

def add_edge(v1,v2):

    if v1 not in nodes:
        print(v1,"is not presented in graph")
    elif v1 not in nodes:
        print(v1,"is not presented in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)

        graph[index1][index2] = 1


nodes = []
graph = []
n_count = 0

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")



add_edge("A","B")
add_edge("A","C")
add_edge("C","D")
add_edge("D","A")
add_edge("D","B")


print(graph)
show()
