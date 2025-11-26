from graph import Graph 

def create_graph():
    graph_valle_real = Graph()

    graph_valle_real.add_edge("A", "B", 257.5)
    graph_valle_real.add_edge("A", "C", 608.1)
    graph_valle_real.add_edge("B", "D", 292.8)
    graph_valle_real.add_edge("D", "F", 156.8)
    graph_valle_real.add_edge("F", "G", 186.7)
    graph_valle_real.add_edge("G", "H", 54.3)
    graph_valle_real.add_edge("H", "I", 80.8)
    graph_valle_real.add_edge("I", "C", 401.3)
    graph_valle_real.add_edge("I", "K", 136.9)
    graph_valle_real.add_edge("K", "L", 333.9)
    graph_valle_real.add_edge("L", "M", 260.7)
    graph_valle_real.add_edge("M", "Z", 158.6)
    graph_valle_real.add_edge("F", "J", 362.8)
    graph_valle_real.add_edge("J", "Z", 548.8)
    graph_valle_real.add_edge("C", "N", 420.5)
    graph_valle_real.add_edge("N", "L", 210.3)

    return graph_valle_real


if __name__ == "__main__":
    graph_valle_real = create_graph()
    
    graph_valle_real.print_graph()
    start = "A"
    print(f"Metodo Dijkstra desde {start}\n")

    distances, previous = graph_valle_real.dijkstra(start)

    print(f"Distancias mas cortas desde {start}:")
    for node, distance in distances.items():
        print(f"{start} -> {node}: {distance} m")
    
    graph_valle_real.print_shortest_path(previous, "A", "Z")


    from visualize import animate_dijkstra
    print("\nAbriendo visualización...\n")
    animate_dijkstra(graph_valle_real, "A", "Z")
