import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import matplotlib.colors as mcolors

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

    def eh_multi(self):
        for v1 in self.vertices:
            vizinhos_vistos = set()
            for v2, _ in self.arestas[v1]:  # percorre os vizinhos do vértice v1
                if v2 in vizinhos_vistos:
                    return True  # Se houver arestas múltiplas, retorna True
                vizinhos_vistos.add(v2)
        return False  # Se não houver arestas múltiplas, retorna False

    def eh_conexo(self):
        if not self.vertices:
            return True
            
        v_inicial = next(iter(self.vertices))
        visitados = set()
        
        def busca(v):
            if v in visitados:
                return
            visitados.add(v)
            for vizinho, peso in self.arestas.get(v, []):  # Desempacotar a tupla corretamente
                busca(vizinho)
        
        busca(v_inicial)
        
        return len(visitados) == len(self.vertices)

    def visualizar(self, titulo="Visualização do Grafo"):
        """Visualiza o grafo usando matplotlib e networkx."""
        # Criar um grafo networkx multi-aresta
        G = nx.MultiGraph()  # Usar MultiGraph para suportar múltiplas arestas

        # Adicionar vértices
        for v in self.vertices:
            G.add_node(v)

        # Adicionar arestas com pesos
        for v in self.arestas:
            for vizinho, peso in self.arestas[v]:
                # Adicionar cada aresta com seu peso
                # Ordenar para evitar adicionar duas vezes
                if v < vizinho:
                    G.add_edge(v, vizinho, weight=peso)

        # Configurar posicionamento dos nós
        pos = nx.spring_layout(G, seed=42)  # Layout de força direcionada com seed fixo

        # Criar figura
        plt.figure(figsize=(10, 7))

        # Desenhar nós
        nx.draw_networkx_nodes(
            G, pos, node_size=700, node_color="skyblue", edgecolors="black"
        )

        # Coletar pesos para criar escala de cores
        edge_weights = [data["weight"] for _, _, data in G.edges(data=True)]
        min_weight = min(edge_weights) if edge_weights else 0
        max_weight = max(edge_weights) if edge_weights else 1
        
        # Desenhar arestas com cores baseadas no peso
        edges = G.edges(data=True)
        
        # Criar colormap normalizado
        if min_weight != max_weight:
            # Modificar o intervalo de normalização para garantir cores mais visíveis para valores baixos
            # Vamos usar 0.3 como valor mínimo de intensidade para garantir que arestas de peso baixo fiquem visíveis
            norm = Normalize(
                vmin=min_weight - 0.3 * (max_weight - min_weight),  # Estender o intervalo para baixo
                vmax=max_weight
            )
            
            # Usar um colormap que tenha bom contraste
            cmap = plt.cm.get_cmap('Blues')
            
            # Desenhar arestas com cores baseadas no peso
            for edge in edges:
                u, v, data = edge
                weight = data['weight']
                color = cmap(norm(weight))
                # Garantir uma cor minimamente visível
                color_hex = mcolors.rgb2hex(color[:3])
                nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=2.5, edge_color=color_hex, alpha=0.8)
        else:
            # Se todos os pesos forem iguais
            nx.draw_networkx_edges(G, pos, width=2.5, edge_color="steelblue", alpha=0.8)
        
        # Adicionar labels nos nós
        nx.draw_networkx_labels(G, pos, font_size=14, font_weight="bold")

        # Obter arestas entre pares de vértices (para lidar com múltiplas arestas)
        edge_pairs = {}
        for u, v, data in G.edges(data=True):
            key = tuple(sorted([u, v]))
            if key in edge_pairs:
                edge_pairs[key].append(data["weight"])
            else:
                edge_pairs[key] = [data["weight"]]
        
        # Preparar labels para arestas
        edge_labels = {}
        for edge, weights in edge_pairs.items():
            if len(weights) > 1:
                # Para arestas múltiplas, mostrar como lista ordenada
                weights.sort()  # Opcional: ordenar os pesos
                edge_labels[edge] = f"{weights}"
            else:
                # Para aresta única, mostrar apenas o número
                edge_labels[edge] = f"{weights[0]}"
        
        # Adicionar labels nas arestas com melhor posicionamento e formatação
        nx.draw_networkx_edge_labels(
            G, 
            pos, 
            edge_labels=edge_labels,
            font_size=10,
            font_color='darkblue',
            font_weight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.8)
        )
        
        # Adicionar barra de cores para indicar o mapeamento de peso
        if min_weight != max_weight:
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
            sm.set_array([])
            cbar = plt.colorbar(sm, ax=plt.gca(), shrink=0.7, aspect=20)
            cbar.set_label("Peso das Arestas", size=12)
        
        # Configurações do plot
        plt.axis("off")  # Remover eixos
        plt.title(titulo, fontsize=16, pad=20)
        plt.tight_layout()

        return plt  # Retorna o objeto plt para personalização adicional

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

    print("\nO grafo tem arestas múltiplas?", g.eh_multi())
    # Adicionar uma aresta múltipla e verificar novamente
    print("\nAdicionando uma aresta múltipla entre os vértices 1 e 2...")
    g.adicionar_aresta(1, 2, 8)  # Já existe uma aresta (1,2) com peso 5

    print("O grafo agora tem arestas múltiplas?", g.eh_multi())

     # Testar se o grafo é conexo
    print("\nVerificando se o grafo é conexo:")
    print("O grafo atual é conexo?", g.eh_conexo())

    # Criar um grafo desconexo adicionando um vértice isolado
    print("\nCriando um grafo desconexo adicionando um vértice isolado...")
    g.adicionar_vertice(7)
    print("O grafo agora é conexo?", g.eh_conexo())

    # Tornar o grafo conexo novamente
    print("\nTornando o grafo conexo novamente...")
    g.adicionar_aresta(6, 7, 2)
    print("O grafo agora é conexo?", g.eh_conexo())

    # Visualizar o grafo
    plt = g.visualizar("Grafo com múltiplas arestas")
    plt.show()
