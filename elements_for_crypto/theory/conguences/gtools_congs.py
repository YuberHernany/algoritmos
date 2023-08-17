import sympy.ntheory as nt
import networkx as nx
import matplotlib.pyplot as plt
plt.style.use("dark_background")

def gclasses_mod(n):
    """
    INPUTS: n (int)
    OUTPUTS: G (networkx graph)
    Create graph without showing it"""
    G = nx.Graph()
    str_n = 'Z'+str(n)
    G.add_node(str_n)
    for k in range(n):
        G.add_edge(k, str_n)

    for k in range(n, 2*n):
        G.add_edge(k, k%n)

    for k in range(2*n, 3*n):
        G.add_edge(k, k%n + n)

    for k in range(3*n, 4*n):
        G.add_edge(k, k%n + 2*n)

    for k in range(4*n, 5*n):
        G.add_edge(k, k%n + 3*n)
    return G

def show_classes(G):
    """create the graphical version of the graph"""
    nx.draw_networkx(G, edge_color='gray', with_labels=True)

def gsum_mod(n, a, b):
    """INPUTS: all type int. n: modulo; a, b: operands
        OUTPUTS: create the graphical explanation for sum"""
    G = gclasses_mod(n)
    color_map = []
    for node in G:
        if node in [a, b]:
            color_map.append('gray')
        elif node in [a+b, (a+b)%n]:
            color_map.append('yellow')
        else:
            color_map.append('green')
    nx.draw(G, node_color=color_map, edge_color='gray', with_labels=1)

def gprod_mod(n, a, b):
    """INPUTS: all type int. n: modulo; a, b: operands
    OUTPUTS: create the graphical explanation for product"""
    G = gclasses_mod(n)
    color_map = []
    for node in G:
        if node in [a, b]:
            color_map.append('gray')
        elif node in [a*b, (a*b)%n]:
            color_map.append('yellow')
        else:
            color_map.append('green')
    nx.draw(G, node_color=color_map, edge_color='gray', with_labels=1)


if __name__ == "__main__":
    pass

