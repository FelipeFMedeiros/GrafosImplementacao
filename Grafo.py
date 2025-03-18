import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}  # Dicionário de adjacências {v: [(vizinho, peso)]}

    def adicionar_vertice(self, v):
        if v not in self.vertices:
            self.vertices.add(v)
            self.arestas[v] = []

    def adicionar_aresta(self, v1, v2, peso=1):
        if v1 in self.vertices and v2 in self.vertices:
            self.arestas[v1].append((v2, peso))
            self.arestas[v2].append((v1, peso))
        else:
            print("Erro: Um dos vértices não existe.")

    def imprimir(self):
        for v in self.arestas:
            print(f"{v} -> {self.arestas[v]}")

    def remover_vertice(self, v):
        if v in self.vertices:
            self.vertices.remove(v)
            del self.arestas[v]
            for adj in self.arestas:
                self.arestas[adj] = [(v2, p) for v2, p in self.arestas[adj] if v2 != v]

    def remover_aresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.arestas[v1] = [(v, p) for v, p in self.arestas[v1] if v != v2]
            self.arestas[v2] = [(v, p) for v, p in self.arestas[v2] if v != v1]

    def a_eh_Adjacente(self, a1, a2):
        v1, u1 = a1  # Primeira aresta (v1--u1)
        v2, u2 = a2  # Segunda aresta (v2--u2)
        return v1 in (v2, u2) or u1 in (v2, u2)

    def v_eh_adjacente(self, v1, v2):
        return any(v2 == vizinho for vizinho, _ in self.arestas.get(v1, []))

    def lista_adjacencia(self, v):
        return self.arestas.get(v, [])

    def grau(self, v):
        return len(self.arestas.get(v, []))

    def eh_regular(self):
        if not self.vertices:
            return True  # Um grafo vazio é considerado regular

        grau_ini = self.grau(
            next(iter(self.vertices))
        )  # salva o grau do primeiro vértice do grafo
        for v in self.vertices:  # verifica o grau do resto dos vértices do grafo
            if self.grau(v) != grau_ini:  # compara se os outros graus com o do primeiro
                return False  # retorna False se algum grau for diferente
        return True  # retorna True se todos os graus forem iguais

    def visualizar(self, titulo="Visualização do Grafo"):
        """Visualiza o grafo usando matplotlib e networkx."""
        # Criar um grafo networkx
        G = nx.Graph()

        # Adicionar vértices
        for v in self.vertices:
            G.add_node(v)

        # Adicionar arestas com pesos
        arestas_adicionadas = set()
        for v in self.arestas:
            for vizinho, peso in self.arestas[v]:
                # Adiciona cada aresta apenas uma vez (evita duplicação)
                aresta = tuple(sorted([v, vizinho]))
                if aresta not in arestas_adicionadas:
                    G.add_edge(v, vizinho, weight=peso)
                    arestas_adicionadas.add(aresta)

        # Configurar posicionamento dos nós
        pos = nx.spring_layout(
            G, seed=42
        )  # Layout de força direcionada com seed fixo para consistência

        # Pesos para labels de arestas
        edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}

        # Criar figura
        plt.figure(figsize=(10, 7))

        # Desenhar nós
        nx.draw_networkx_nodes(
            G, pos, node_size=700, node_color="skyblue", edgecolors="black"
        )

        # Desenhar arestas
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color="gray")

        # Adicionar labels nos nós
        nx.draw_networkx_labels(G, pos, font_size=14, font_weight="bold")

        # Adicionar labels nas arestas (pesos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

        # Configurações do plot
        plt.axis("off")  # Remover eixos
        plt.title(titulo, fontsize=16)
        plt.tight_layout()

        return plt  # Retorna o objeto plt para permitir personalização adicional


# Exemplo de uso
if __name__ == "__main__":
    # Criar grafo de exemplo
    g = Grafo()

    # Adicionar vértices
    for i in range(1, 7):
        g.adicionar_vertice(i)

    # Adicionar arestas com pesos
    g.adicionar_aresta(1, 2, 5)
    g.adicionar_aresta(1, 3, 3)
    g.adicionar_aresta(2, 3, 1)
    g.adicionar_aresta(2, 4, 7)
    g.adicionar_aresta(3, 5, 2)
    g.adicionar_aresta(4, 5, 4)
    g.adicionar_aresta(4, 6, 6)
    g.adicionar_aresta(5, 6, 8)

    # Mostrar informações do grafo
    print("Representação do grafo:")
    g.imprimir()

    print("\nVerificando adjacência entre arestas:")
    print("(1, 2) e (2, 3) são adjacentes?", g.a_eh_Adjacente((1, 2), (2, 3)))
    print("(1, 2) e (5, 6) são adjacentes?", g.a_eh_Adjacente((1, 2), (5, 6)))

    print("\nVerificando adjacência entre vértices:")
    print("1 e 2 são adjacentes?", g.v_eh_adjacente(1, 2))
    print("1 e 6 são adjacentes?", g.v_eh_adjacente(1, 6))

    print("\nLista de adjacência do vértice 3:", g.lista_adjacencia(3))

    print("\nGraus dos vértices:")
    for v in g.vertices:
        print(f"Grau do vértice {v}: {g.grau(v)}")

    print("\nO grafo é regular?", g.eh_regular())

    # Visualizar o grafo
    plt = g.visualizar("Grafo de Exemplo")
    plt.show()
