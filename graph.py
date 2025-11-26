class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph: # si el nodo no existe en el grafo, lo creamos con una lista vacia
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append((v, weight)) # agregamos conecion de u a v con su distancia
        self.graph[v].append((u, weight)) # agregamos conexion de v a u con el mismo peso

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph} # Diccionario con las distancias mas cortas
        distances[start] = 0 # El nodo inicial le ponemos distancia de 0 porque no hay distancia hacia el mismo

        visited = [] # Array para guardar los nodos que ya visitamos

        previous_path =  {node: None for node in self.graph} # Guardar el camino anterior

        while len(visited) < len(self.graph): # Mientras no hemos visitado todos los nodos
            min_non_visited_node = None
            for node in self.graph:
                if node not in visited:
                    if min_non_visited_node is None or distances[node] < distances[min_non_visited_node]: # buscar el nodo no visitado con la distancia mas corta
                        min_non_visited_node = node
            
            if min_non_visited_node is None: # si ya no hay nodos por visitar terminar el for
                break
        
            for neighbor, weight in self.graph[min_non_visited_node]: # recorrer vecinos del nodo actual
                new_distance = round(distances[min_non_visited_node] + weight, 2) # nueva distancia al vecino tomando en cuenta el nodo actual
                if new_distance < distances[neighbor]: # si la nueva distancia es menor que la que ya teniamos
                    distances[neighbor] = new_distance # guardar la nueva distancia
                    previous_path[neighbor] = min_non_visited_node
            visited.append(min_non_visited_node) # marcar el nodo como visitado
        return distances, previous_path

    def print_graph(self):
        print("Grafo:\n")
        for node, edges in self.graph.items():     # recorremos todos los nodos y sus conexiones
            print(f"{node}: {edges}")
    
    def print_shortest_path(self, previous_path, start, end):
        path = [] # guardar el camino
        current = end # comenzar desde el nodo final, de meta a inicio
        while current is not None:
            path.insert(0, current) # insertamos cada nodo al inicio de la lista
            current = previous_path[current] # y mos movemos al nodo anterior
        print(f"Ruta mas corta de {start} a {end}: {' -> '.join(path)}")
