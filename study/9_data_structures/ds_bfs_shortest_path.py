class Graph:
    def bfs_path(self, start, end):
        visited = []
        to_visit = [[start]]

        while to_visit:
            path = to_visit.pop(0) # take the first path in the list
            current = path[-1] # take the last element in the path-list, this is our current location

            if current not in visited:
                visited.append(current)
            
                if current == end:
                    return path # we found our path
                
                neighbors = sorted(self.graph.get(current, [])) # return an empty list if there is no result
                for neighbor in neighbors:
                    if neighbor not in visited: # this means a new potential path
                        new_path = list(path)
                        new_path.append(neighbor)
                        to_visit.append(new_path)
        
        return None #if no path is found

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])
    
    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

g = Graph()
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("D", "E")
g.add_edge("C", "E")
g.add_edge("A", "E")
g.add_edge("E", "C")
g.add_edge("B", "F")

print(g.bfs_path("A", "F"))  # Output should be a valid path, e.g., ['A', 'B', 'D', 'E', 'F']