import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx

# Construir grafo de NetworkX a partir de clase Graph
def build_networkx_graph(custom_graph):
    G = nx.Graph()
    for node, edges in custom_graph.graph.items():
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)
    return G

# Dijkstra con pasos guardados para animación
def dijkstra_steps(graph_obj, start):
    distances = {node: float("inf") for node in graph_obj.graph}
    distances[start] = 0
    visited = []
    previous = {node: None for node in graph_obj.graph}

    steps = []

    while len(visited) < len(graph_obj.graph):

        current = None
        for node in graph_obj.graph:
            if node not in visited:
                if current is None or distances[node] < distances[current]:
                    current = node

        if current is None:
            break

        # Guardar antes de expandir
        steps.append(("visiting", current, distances.copy(), visited.copy(), previous.copy()))

        # Actualizar vecinos
        for neighbor, weight in graph_obj.graph[current]:
            new_dist = distances[current] + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current

        visited.append(current)

        # Guardar después
        steps.append(("updated", current, distances.copy(), visited.copy(), previous.copy()))

    return distances, previous, steps

# Sacar camino final
def extract_path(previous, start, end):
    path = []
    node = end
    while node is not None:
        path.insert(0, node)
        node = previous[node]
    return path

# Animación principal
def animate_dijkstra(graph_obj, start, end):
    G = build_networkx_graph(graph_obj)
    pos = nx.spring_layout(G, seed=42)

    distances, previous, steps = dijkstra_steps(graph_obj, start)
    shortest_path = extract_path(previous, start, end)

    fig, ax = plt.subplots(figsize=(10, 7))

    def update(i):
        ax.clear()

        step_type, current, dist, visited, prev = steps[i]

        colors = []
        for node in G.nodes():
            if node == current:
                colors.append("yellow")
            elif node in visited:
                colors.append("lightgreen")
            else:
                colors.append("skyblue")

        edge_colors = []
        for u, v in G.edges():

            # Camino final (rojo)
            if (
                u in shortest_path
                and v in shortest_path
                and abs(shortest_path.index(u) - shortest_path.index(v)) == 1
            ):
                edge_colors.append("red")
                continue

            # Arista explorada en este paso (naranja)
            if step_type == "visiting" and (u == current or v == current):
                edge_colors.append("orange")
                continue

            # Aristas ya visitadas (verde claro)
            if u in visited and v in visited:
                edge_colors.append("lightgreen")
                continue

            # Aristas no tocadas
            edge_colors.append("gray")

        # Dibujar grafo con colores actualizados
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color=colors,
            edge_color=edge_colors,
            node_size=800,
            ax=ax,
            font_size=10
        )
        
        # ---- MOSTRAR PESOS DE ARISTAS ----
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, ax=ax)

        ax.set_title(f"Paso {i+1}/{len(steps)} - Nodo actual: {current}")

        # Mostrar distancias a la derecha
        text = "\n".join([f"{n}: {round(dist[n], 2)}" for n in dist])
        ax.text(
            1.05,
            0.1,
            text,
            transform=ax.transAxes,
            fontsize=10,
            bbox=dict(facecolor="white", alpha=0.7)
        )

    # Animación
    ani = animation.FuncAnimation(
        fig, update, frames=len(steps), interval=1200, repeat=False
    )

    plt.show()

if __name__ == "__main__":
    from main import create_graph

    graph_valle_real = create_graph()
    animate_dijkstra(graph_valle_real, "A", "Z")
