import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import matplotlib.colors as mcolors


class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}  # Dicionário de adjacências {v: [(vizinho, peso)]}

    # Adicionar um vértice ao grafo
    def adicionar_vertice(self, v):
        if v not in self.vertices:
            self.vertices.add(v) # type: ignore
            self.arestas[v] = []

    # Adicionar uma aresta entre dois vértices
    def adicionar_aresta(self, v1, v2, peso=1):
        if v1 in self.vertices and v2 in self.vertices:
            self.arestas[v1].append((v2, peso))
            self.arestas[v2].append((v1, peso))
        else:
            print("Erro: Um dos vértices não existe.")

    # Imprimir o grafo
    def imprimir(self):
        for v in self.arestas:
            print(f"{v} -> {self.arestas[v]}")

    #Recebendo formalismo
    def g_form(self, vertices, arestas):
        self.vertices = set(vertices)
        self.arestas = {v: [] for v in vertices}  # iniciando a lista

        for v1, v2, peso in arestas:
            self.arestas[v1].append((v2, peso))
            self.arestas[v2].append((v1, peso))

        return self.imprimir()

    # Remover um vértice do grafo
    def remover_vertice(self, v):
        if v in self.vertices:
            self.vertices.remove(v)
            del self.arestas[v]
            for adj in self.arestas:
                self.arestas[adj] = [(v2, p) for v2, p in self.arestas[adj] if v2 != v]

    # Remover uma aresta entre dois vértices
    def remover_aresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.arestas[v1] = [(v, p) for v, p in self.arestas[v1] if v != v2]
            self.arestas[v2] = [(v, p) for v, p in self.arestas[v2] if v != v1]

    # Converte o grafo para uma matriz de adjacência
    def g_form_mAdj(self):
        """Converte o grafo para uma matriz de adjacência"""
        n = len(self.vertices)
        mAdj = [[0] * (n + 1) for _ in range(n + 1)]  # Matriz de (n+1)x(n+1) para índices 1 a n vértices

        for v in self.arestas:
            for u, w in self.arestas[v]:
                mAdj[v][u] = w
                mAdj[u][v] = w  # Grafo não direcionado

        return mAdj

    # Converte o formalismo em lista de adjacência
    def g_form_lAdj(self, vertices, arestas):
        """
        Convertendo o formalismo G(V,A,w) para uma lista de adjacência
        v -> lista de vértices [v1, v2, v3, ...]
        a -> lista de tuplas [(v1, v2, peso), (v2, v3, peso), ...]
        """
        self.vertices = set(vertices)
        self.arestas = {v: [] for v in vertices}  # iniciando a lista

        for v1, v2, peso in arestas:
            self.arestas[v1].append((v2, peso))
            self.arestas[v2].append((v1, peso))
            print('Converão concluída')

    # Converte o formalismo em matriz de incidência
    def g_form_mInc(self, vertices, arestas):
        """
        Converte um grafo dado no formalismo G(V, A, w) para uma matriz de incidência.

        :param vertices: Lista de vértices [v1, v2, v3, ...]
        :param arestas: Lista de tuplas [(v1, v2, peso), (v2, v3, peso), ...]
        """
        self.vertices = list(vertices)  # Lista para manter ordem dos vértices
        num_vertices = len(vertices)
        num_arestas = len(arestas)

        # Criar matriz n x m preenchida com zeros
        m = [[0] * num_arestas for _ in range(num_vertices)]

        # Criar um mapeamento vértice -> índice da matriz
        indice_vertice = {v: i for i, v in enumerate(self.vertices)}

        # Preencher matriz de incidência
        for j, (v1, v2, peso) in enumerate(arestas):  # j é o índice da aresta
            i1 = indice_vertice[v1]  # Índice do vértice v1
            i2 = indice_vertice[v2]  # Índice do vértice v2
            m[i1][j] = 1
            m[i2][j] = 1

        # Armazena a matriz no grafo
        self.matriz_incidencia = m
        print("Conversão para matriz de incidência concluída!")

        return m

    # Verifica se duas arestas são adjacentes
    def a_eh_Adjacente(self, a1, a2):
        v1, u1 = a1  # Primeira aresta (v1--u1)
        v2, u2 = a2  # Segunda aresta (v2--u2)
        return v1 in (v2, u2) or u1 in (v2, u2)

    # Verifica se dois vértices são adjacentes
    def v_eh_adjacente(self, v1, v2):
        return any(v2 == vizinho for vizinho, _ in self.arestas.get(v1, []))

    # Retorna a lista de adjacência de um vértice
    def lista_adjacencia(self, v):
        """
        Imprime a lista de adjacência de um vértice.
    # Retorna a lista de adjacência de um vértice
    def lista_adjacencia(self, v):

        Imprime a lista de adjacência de um vértice.

        :param v: O vértice para o qual imprimir a lista de adjacência
        :return: A lista de adjacência (para manter compatibilidade)
        """
        adjacentes = self.arestas.get(v, [])
        if v in self.vertices:
            if adjacentes:
                print(f"Vértice {v} é adjacente a: {[vizinho for vizinho, _ in adjacentes]}")
            else:
                print(f"Vértice {v} não possui vértices adjacentes")
        else:
            print(f"Vértice {v} não existe no grafo")
        return adjacentes

    # Retorna o grau de um vértice
    def grau(self, v):
        return len(self.arestas.get(v, []))

    # Verifica se o grafo é regular
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

    # Verifica se o grafo tem arestas múltiplas
    def eh_multi(self):
        for v1 in self.vertices:
            vizinhos_vistos = set()
            for v2, _ in self.arestas[v1]:  # percorre os vizinhos do vértice v1
                if v2 in vizinhos_vistos:
                    return True  # Se houver arestas múltiplas, retorna True
                vizinhos_vistos.add(v2)
        return False  # Se não houver arestas múltiplas, retorna False

    # Verifica se o grafo é conexo
    def eh_conexo(self):
        if not self.vertices:
            return True

        v_inicial = next(iter(self.vertices))
        visitados = set()

    def busca(self, v, visitados):
        if v in visitados:
            return

        visitados.add(v)
        for vizinho, peso in self.arestas.get(v, []):  # Desempacotar a tupla corretamente
            self.busca(vizinho)

        self.busca(self.v_inicial)

        return len(visitados) == len(self.vertices)

    # Verifica se o grafo é completo
    def eh_completo(self):
        """
        Verifica se o grafo é completo.
        Um grafo é completo se todos os vértices estão conectados entre si.
        """
        if not self.vertices or len(self.vertices) == 1:
            return True  # Grafo vazio ou com apenas um vértice é considerado completo

        n = len(self.vertices)  # Número de vértices
        # Em um grafo completo, cada vértice deve ter grau n-1
        for v in self.vertices:
            # Contamos apenas vértices únicos para ignorar arestas múltiplas
            vizinhos_unicos = set(vizinho for vizinho, _ in self.arestas.get(v, []))
            if len(vizinhos_unicos) != n - 1:
                return False
        return True


    # Retorna os vértices incidentes de uma aresta
    # Verifica se o grafo é bipartido
    def eh_bipartido(self):
        """
        Verifica se o grafo é bipartido.
        Um grafo é bipartido se seus vértices podem ser divididos em dois grupos
        de modo que não haja arestas entre vértices do mesmo grupo.
        """
        if not self.vertices:
            return True  # Um grafo vazio é considerado bipartido

        # Dicionário para armazenar as cores dos vértices (0 ou 1)
        cores = {}

        # Para cada componente conexo
        for vertice_inicial in self.vertices:
            if vertice_inicial in cores:
                continue  # Vértice já foi colorido

            # Iniciar BFS a partir deste vértice
            fila = [vertice_inicial]
            cores[vertice_inicial] = 0  # Atribuir cor inicial

            while fila:
                atual = fila.pop(0)
                cor_atual = cores[atual]

                # Verificar todos os vizinhos
                for vizinho, _ in self.arestas.get(atual, []):
                    if vizinho not in cores:
                        # Atribuir cor oposta ao vizinho
                        cores[vizinho] = 1 - cor_atual
                        fila.append(vizinho)
                    elif cores[vizinho] == cor_atual:
                        # Se o vizinho já tem a mesma cor, o grafo não é bipartido
                        return False

        return True

    # Retorna os vértices incidentes de uma aresta
    def a_lInc(self, aresta):
        """
        Retorna os vértices incidentes de uma aresta.
        """
        v1, v2 = aresta

        # Verifica se ambos os vértices existem no grafo
        if v1 not in self.vertices or v2 not in self.vertices:
            return []

        # Verifica se a aresta existe no grafo
        if any(v2 == vizinho for vizinho, _ in self.arestas.get(v1, [])):
            return [v1, v2]
        else:
            return []  # A aresta não existe no grafo

    # Converte uma matriz de adjacência para lista de adjacência
    def g_mAdj_lAdj(self, matriz_adj):
        """
        Converte uma matriz de adjacência para lista de adjacência.

        :param matriz_adj: Matriz de adjacência (lista de listas)
        :return: Um novo grafo com a representação em lista de adjacência
        """
        # Criar um novo grafo para armazenar a lista de adjacência
        grafo = Grafo()

        # O tamanho da matriz é o número de vértices
        n = len(matriz_adj)

        # Adicionar vértices
        # A matriz pode começar com índice 0 ou 1, dependendo da convenção
        # Verificamos se a primeira linha/coluna tem dados significativos
        tem_indice_zero = any(matriz_adj[0]) if n > 0 else False

        # Adicionar vértices com base na matriz
        inicio = 0 if tem_indice_zero else 1
        for i in range(inicio, n):
            grafo.adicionar_vertice(i)

        # Adicionar arestas com base na matriz
        for i in range(inicio, n):
            for j in range(inicio, n):
                peso = matriz_adj[i][j]
                if peso > 0:  # Se há uma aresta
                    # Adicionar apenas uma vez, já que grafo é não direcionado
                    if i < j:  # Evita adicionar a mesma aresta duas vezes
                        grafo.adicionar_aresta(i, j, peso)

        return grafo

    # Converte uma matriz de adjacência para matriz de incidência
    def g_mAdj_mInc(self, matriz_adj):
        """
        Converte uma matriz de adjacência para uma matriz de incidência.

        :param matriz_adj: Matriz de adjacência (lista de listas)
        :return: A matriz de incidência resultante e lista de arestas [(v1,v2,peso),...]
        """
        # O tamanho da matriz é o número de vértices
        n = len(matriz_adj)

        # A matriz pode começar com índice 0 ou 1, dependendo da convenção
        # Verificamos se a primeira linha/coluna tem dados significativos
        tem_indice_zero = any(matriz_adj[0]) if n > 0 else False
        inicio = 0 if tem_indice_zero else 1

        # Coletar todas as arestas da matriz de adjacência
        arestas = []
        for i in range(inicio, n):
            for j in range(i+1, n):  # Só precisamos da metade superior da matriz (grafo não direcionado)
                peso = matriz_adj[i][j]
                if peso > 0:
                    arestas.append((i, j, peso))

        # Criar a matriz de incidência (vértices × arestas)
        num_vertices = n - inicio
        num_arestas = len(arestas)
        matriz_inc = [[0] * num_arestas for _ in range(num_vertices)]

        # Preencher a matriz de incidência
        for idx_aresta, (v1, v2, _) in enumerate(arestas):
            # Ajustar índices se necessário
            v1_idx = v1 - inicio
            v2_idx = v2 - inicio

            # Marcar os vértices incidentes a esta aresta
            matriz_inc[v1_idx][idx_aresta] = 1
            matriz_inc[v2_idx][idx_aresta] = 1

        return matriz_inc, arestas


    #Função que implementa a conversão de uma Matriz Incidência para o formalismo
    def g_mInc_form(self):
        """
        n  -> representam os vértices
        m -> representam as arestas
         Segue uma ideia similar a conversão do formalismo para a matriz de incidência
         Preciso gerar a lista de arestas na forma (v1, v2, peso), assumindo o peso padrão como 1
        """
        num_vertices = len(self.matriz_incidencia)
        num_arestas = len(self.matriz_incidencia[0]) if num_vertices > 0 else 0

        #Criar lista de vértices
        vertices = list(self.vertices)

        #Criar uma lista de arestas
        arestas = []

        for j in range(num_arestas): #percorre cada coluna (arestas)
            vertices_conectados = [i for i in range(num_vertices) if self.matriz_incidencia[i][j]==1]

            if len(vertices_conectados) == 2: #deve haver exatamente dois vértices conectados
                v1, v2 = vertices[vertices_conectados[0]], vertices[vertices_conectados[1]]
                arestas.append((v1,v2, 1)) #Peso 1 por padrão

        print("A conversão da matriz de incidência para formalismo foi concluída")
        return vertices, arestas



    # Converte uma matriz de adjacência para formalismo G(V,(A,w))
    def g_mAdj_form(self, matriz_adj):
        """
        Converte uma matriz de adjacência para o formalismo G(V,(A,w)).

        :param matriz_adj: Matriz de adjacência (lista de listas)
        :return: Uma tupla (vertices, arestas) onde vertices é uma lista de vértices
                e arestas é uma lista de tuplas (v1, v2, peso)
        """
        # O tamanho da matriz é o número de vértices
        n = len(matriz_adj)

        # A matriz pode começar com índice 0 ou 1, dependendo da convenção
        # Verificamos se a primeira linha/coluna tem dados significativos
        tem_indice_zero = any(matriz_adj[0]) if n > 0 else False
        inicio = 0 if tem_indice_zero else 1

        # Criar lista de vértices
        vertices = list(range(inicio, n))

        # Coletar todas as arestas da matriz de adjacência
        arestas = []
        for i in range(inicio, n):
            for j in range(i+1, n):  # Só precisamos da metade superior da matriz (grafo não direcionado)
                peso = matriz_adj[i][j]
                if peso > 0:
                    arestas.append((i, j, peso))

        return vertices, arestas

    # Converte uma matriz de incidência para lista de adjacência
    def g_mInc_mAdj(self, matriz_inc=None):
        """
        Converte uma matriz de incidência para uma matriz de adjacência.

        :param matriz_inc: Matriz de incidência (se None, usa self.matriz_incidencia)
        :return: A matriz de adjacência resultante
        """
        # Usar a matriz armazenada se não fornecida
        if matriz_inc is None:
            if not hasattr(self, 'matriz_incidencia'):
                raise ValueError("Nenhuma matriz de incidência encontrada no grafo")
            matriz_inc = self.matriz_incidencia

        # Obter número de vértices e arestas
        num_vertices = len(matriz_inc)
        num_arestas = len(matriz_inc[0]) if matriz_inc and matriz_inc[0] else 0

        # Criar matriz de adjacência vazia
        matriz_adj = [[0] * num_vertices for _ in range(num_vertices)]

        # Para cada aresta (coluna na matriz de incidência)
        for j in range(num_arestas):
            # Encontrar os vértices incidentes a esta aresta
            vertices_incidentes = []
            for i in range(num_vertices):
                if matriz_inc[i][j] == 1:
                    vertices_incidentes.append(i)

            # Se encontrarmos exatamente 2 vértices, adicionar à matriz de adjacência
            if len(vertices_incidentes) == 2:
                v1, v2 = vertices_incidentes
                matriz_adj[v1][v2] = 1
                matriz_adj[v2][v1] = 1  # Grafo não direcionado

        return matriz_adj

    # Converte uma matriz de incidência para formalismo G(V,(A,w))
    def g_mInc_lAdj(self, matriz_inc=None):
        """
        Converte uma matriz de incidência para uma representação em lista de adjacência.

        :param matriz_inc: Matriz de incidência (se None, usa self.matriz_incidencia)
        :return: Um novo grafo com a representação em lista de adjacência
        """
        # Usar a matriz armazenada se não fornecida
        if matriz_inc is None:
            if not hasattr(self, 'matriz_incidencia'):
                raise ValueError("Nenhuma matriz de incidência encontrada no grafo")
            matriz_inc = self.matriz_incidencia

        # Obter número de vértices e arestas
        num_vertices = len(matriz_inc)
        num_arestas = len(matriz_inc[0]) if matriz_inc and matriz_inc[0] else 0

        # Criar um novo grafo para armazenar o resultado
        grafo_resultante = Grafo()

        # Define o índice inicial dos vértices (0 ou 1)
        indice_inicial = 0  # Assume que os vértices são indexados a partir de 0

        # Adicionar vértices
        for i in range(indice_inicial, indice_inicial + num_vertices):
            grafo_resultante.adicionar_vertice(i)

        # Para cada aresta (coluna na matriz de incidência)
        for j in range(num_arestas):
            # Encontrar os vértices incidentes a esta aresta
            vertices_incidentes = []
            for i in range(num_vertices):
                if matriz_inc[i][j] == 1:
                    vertices_incidentes.append(i + indice_inicial)

            # Se encontrarmos exatamente 2 vértices, adicionar aresta
            if len(vertices_incidentes) == 2:
                v1, v2 = vertices_incidentes
                # Como não temos informação de peso na matriz de incidência básica,
                # usamos 1 como padrão
                grafo_resultante.adicionar_aresta(v1, v2, 1)

        return grafo_resultante

    # Função extra de visualização do grafo
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


# Exemplo mínimo de uso | Exemlo real no arquivo exemplo_grafo.py
if __name__ == "__main__":
    # Criar um pequeno exemplo
    g = Grafo()
    vertices = [1, 2, 3, 4, 5, 6]
    arestas = [(1, 2, 5), (2, 3, 7), (3, 4, 2), (1, 4, 10), (4, 5, 8), (5, 6, 11), (3, 6, 12)]
    matriz_incidencia = [
        [1,0,0],
        [1,1,0],
        [0,1,1],
        [0,0,1]
    ]
    g.vertices = set(vertices)
    g.matriz_incidencia = matriz_incidencia
    v_formalismo, a_formalismo = g.g_mInc_form()

    print(f"Vértices: {v_formalismo}\nArestas: {a_formalismo}")

    # g.adicionar_vertice(1)
    # g.adicionar_vertice(2)
    # g.adicionar_vertice(3)
    # g.adicionar_aresta(1, 2, 5)
    # g.adicionar_aresta(2, 3, 3)
    # g.adicionar_aresta(3, 1, 3)

    print("Lista de adjacência:")
    g.g_form_lAdj(vertices, arestas)

    print("Grafo básico:")
    g.imprimir()
    g.visualizar("Exemplo básico").show()