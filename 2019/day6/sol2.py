import queue  
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])


class GraphUndirectedWeighted(object):  
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v


def dijkstra(graph, source, dest):  
    q = queue.PriorityQueue()
    parents = []
    distances = []
    start_weight = float("inf")

    for i in graph.get_vertex():
        weight = start_weight
        if source == i:
            weight = 0
        distances.append(weight)
        parents.append(None)

    q.put(([0, source]))

    while not q.empty():
        v_tuple = q.get()
        v = v_tuple[1]

        for e in graph.get_edge(v):
            candidate_distance = distances[v] + e.weight
            if distances[e.vertex] > candidate_distance:
                distances[e.vertex] = candidate_distance
                parents[e.vertex] = v
                # primitive but effective negative cycle detection
                if candidate_distance < -1000:
                    raise Exception("Negative cycle detected")
                q.put(([distances[e.vertex], e.vertex]))

    shortest_path = []
    end = dest
    while end is not None:
        shortest_path.append(end)
        end = parents[end]

    shortest_path.reverse()

    return shortest_path, distances[dest]



filename = 'input.txt'
V = set()
E = {}

with open(filename, 'r') as f:
    for l in f:
      node,edge = l.split(')')[0], l.split(')')[1].strip()
      V.add(node)
      V.add(edge)
      if node not in E.keys():
          E[node]=[]
      E[node]+=[edge]



if __name__=='__main__':
    V_d,i = {},0
    for k in V:
        V_d[k]=i
        i+=1
    g = GraphUndirectedWeighted(max(V_d.values())+1)
    print(max(V_d.values()))
    for e in E.keys():
      for el in E[e]:
        g.add_edge(V_d[e],V_d[el],1) 
    shortest_path, distance = dijkstra(g, V_d['YOU'], V_d['SAN'])
    print(distance-2)
      
