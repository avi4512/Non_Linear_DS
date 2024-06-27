def add_node(v):

    if v in graph:
        print(v,"is already presented in the graph")
    else:
        graph[v] = []

def add_edge(v1,v2,weight):

    if v1 not in graph:
        print(v1,'is not presented in graph')
    elif v2 not in graph:
        print(v2,'is not presented in graph')
    else:
        list1 = [v2,weight]
        list2 = [v1,weight]
        graph[v1].append(list1)
        graph[v2].append(list2)



graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A","B",5)
add_edge("A","C",4)
add_edge("A","D",10)
add_edge("B","D",1)
add_edge("B","E",3)
add_edge("C","D",7)
add_edge("D","E",2)
print(graph)