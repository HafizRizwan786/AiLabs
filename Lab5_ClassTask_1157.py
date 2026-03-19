from collections import deque
import matplotlib.pyplot as plt
import networkx as nx
"""
# Task 1
class Graph:
    def __init__(self):
        self.edges = {}
        
    def add_Vertex(self,vertex):
        self.edges[vertex] = deque()
        
    def add_Edge(self,u,v):
        if v not in self.edges[u]:
            self.edges[u].append(v)
            
        if u not in self.edges[v]:
            self.edges[v].append(u)


    def Display (self):
        for vertex,neighbors in self.edges.items():
            print(f"{vertex} : {list(neighbors)} ")
            
                                        
                                        
G1 = Graph()
G1.add_Vertex(1)
G1.add_Vertex(2)
G1.add_Vertex(3)
G1.add_Vertex(4)

G1.add_Edge(1,2)
G1.add_Edge(1,3)
G1.add_Edge(2,3)
G1.add_Edge(1,4)
G1.add_Edge(4,3)
G1.add_Edge(4,2)

G1.Display()



# Task 2
vertices = ["Seattle", "San Francisco", "Los Angeles", "Denver", "Kansas City", "Chicago", "Boston", "New York", "Atlanta", "Miami", "Dallas", "Houston"]

edges = [
[0, 1], [0, 3], [0, 5],# Seattle - San Francisco, Denver, Chicago
[1, 2], [1, 3], # San Francisco - Los Angeles, Denver
[2, 3], [2, 4], [2, 10],# Los Angeles - Denver, Kansas City, Dallas
[3, 4], [3, 5], # Denver - Kansas City, Chicago
[4, 5], [4, 7], [4, 8], [4, 10],# Kansas City - Chicago, New York, Atlanta, Dallas
[5, 6], [5, 7], # Chicago - Boston, New York
[6, 7], # Boston - New York
[7, 8], # New York - Atlanta
[8, 9], [8, 10], [8, 11], # Atlanta - Miami, Dallas, Houston
[9, 11],# Miami - Houston
[10, 11]# Dallas - Houston
]


g2 = Graph()

for vertex in vertices:
    g2.add_Vertex(vertex)
    
for edge in edges:
    g2.add_Edge(vertices[edge[0]],vertices[edge[1]])
    


G = nx.Graph()
G.add_nodes_from(vertices)
nx.edges = [(vertices[u],vertices[v]) for u,v in edges]

G.add_edges_from(nx.edges)
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
plt.show()

"""

# Task 3
romania = {
    'Sibiu': ['Fagaras', 'Rimnicu Vilcea'],
    'Fagaras': ['Bucharest'],
    'Rimnicu Vilcea': ['Pitesti'],
    'Pitesti': ['Bucharest']
}

def breath_first(start,goal,romania):
    frontier=[start]
    previous={start:None}
    
    while frontier:
        current=frontier.pop(0)
        
        if current==goal:
            path=[]
            while current is not None:
                path.append(current)
                current=previous[current]
            return path[::-1]
    
        for neighbor in romania.get(current, []):
            if neighbor not in previous:
                frontier.append(neighbor)
                previous[neighbor] = current
                    
    return []


start_state = 'Sibiu'
goal_state = 'Bucharest'
result = breath_first(start_state, goal_state, romania)
print(result)

G = nx.from_dict_of_lists(romania)
nx.draw_networkx(G,node_size=1000,node_color='red')
plt.show()

