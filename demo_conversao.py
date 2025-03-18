from Grafo import Grafo
import matplotlib.pyplot as plt

# Demonstração de conversão de matriz de adjacência para lista de adjacência
print("Demonstração de conversão de matriz de adjacência para lista de adjacência")
print("=" * 70)

# Criar uma matriz de adjacência para teste (representando um grafo com 6 vértices)
# A linha e coluna de índice 0 são apenas para facilitar a indexação (não usadas)
matriz_adj = [
    [0, 0, 0, 0, 0, 0, 0],  # linha de índice 0
    [0, 0, 5, 3, 0, 0, 0],  # conexões do vértice 1
    [0, 5, 0, 1, 7, 0, 0],  # conexões do vértice 2
    [0, 3, 1, 0, 0, 2, 0],  # conexões do vértice 3
    [0, 0, 7, 0, 0, 4, 6],  # conexões do vértice 4
    [0, 0, 0, 2, 4, 0, 8],  # conexões do vértice 5
    [0, 0, 0, 0, 6, 8, 0]   # conexões do vértice 6
]

# Exibir a matriz de adjacência
print("\nMatriz de adjacência:")
for i in range(1, len(matriz_adj)):
    print(f"{i}: {matriz_adj[i][1:]}")

# Criar um grafo para realizar a conversão
grafo = Grafo()

# Converter a matriz de adjacência para lista de adjacência
grafo_convertido = grafo.g_mAdj_lAdj(matriz_adj)
print("\nGrafo convertido (representação em lista de adjacência):")
grafo_convertido.imprimir()

# Verificar propriedades do grafo convertido
print("\nPropriedades do grafo convertido:")
print(f"É conexo? {grafo_convertido.eh_conexo()}")
print(f"É completo? {grafo_convertido.eh_completo()}")
print(f"É regular? {grafo_convertido.eh_regular()}")
print(f"É bipartido? {grafo_convertido.eh_bipartido()}")
print(f"É multigrafo? {grafo_convertido.eh_multi()}")

# Exibir graus dos vértices
print("\nGraus dos vértices:")
for v in sorted(grafo_convertido.vertices):
    print(f"Grau do vértice {v}: {grafo_convertido.grau(v)}")

# Visualizar o grafo
plt = grafo_convertido.visualizar("Grafo convertido de matriz para lista de adjacência")
plt.show()


#########################################################################################


# Teste de conversão de matriz de adjacência para matriz de incidência
print("\n" + "=" * 70)
print("Demonstração de conversão de matriz de adjacência para matriz de incidência")
print("=" * 70)

# Usamos a mesma matriz de adjacência definida anteriormente

# Converter para matriz de incidência
matriz_inc, arestas = grafo.g_mAdj_mInc(matriz_adj)

# Exibir a lista de arestas encontradas
print("\nArestas identificadas na matriz de adjacência:")
for idx, (v1, v2, peso) in enumerate(arestas):
    print(f"Aresta {idx+1}: ({v1}, {v2}) com peso {peso}")

# Exibir a matriz de incidência resultante
print("\nMatriz de Incidência resultante:")
print("Linhas = Vértices, Colunas = Arestas")
print("     ", end="")
for i in range(len(arestas)):
    print(f"A{i+1:2} ", end="")
print()

# Define se a matriz começa a indexar do zero ou do um
tem_indice_zero = any(matriz_adj[0]) if len(matriz_adj) > 0 else False

for i, linha in enumerate(matriz_inc):
    # Ajustar índice do vértice baseado na convenção da matriz original
    idx_vertice = i + (0 if tem_indice_zero else 1)
    print(f"V{idx_vertice:2}: {linha}")

# Criar um grafo a partir da matriz de incidência para visualização
# (Note que precisaríamos implementar g_mInc_lAdj para fazer isso diretamente)
grafo_da_inc = Grafo()
for v1, v2, peso in arestas:
    if v1 not in grafo_da_inc.vertices:
        grafo_da_inc.adicionar_vertice(v1)
    if v2 not in grafo_da_inc.vertices:
        grafo_da_inc.adicionar_vertice(v2)
    grafo_da_inc.adicionar_aresta(v1, v2, peso)

# Visualizar o grafo
plt = grafo_da_inc.visualizar("Grafo construído a partir da matriz de incidência")
plt.show()


#########################################################################################


# Teste de conversão de matriz de adjacência para formalismo G(V,(A,w))
print("\n" + "=" * 70)
print("Demonstração de conversão de matriz de adjacência para formalismo G(V,(A,w))")
print("=" * 70)

# Usamos a mesma matriz de adjacência definida anteriormente

# Converter para formalismo
vertices, arestas = grafo.g_mAdj_form(matriz_adj)

# Exibir o formalismo resultante
print("\nFormalismo G(V,(A,w)) resultante:")
print(f"V = {vertices}")
print("A = {")
for v1, v2, peso in arestas:
    print(f"  ({v1}, {v2}, {peso})")
print("}")

# Criar um novo grafo a partir do formalismo para verificar
print("\nCriando um novo grafo a partir do formalismo...")
grafo_do_formalismo = Grafo()
for v in vertices:
    grafo_do_formalismo.adicionar_vertice(v)
    
for v1, v2, peso in arestas:
    grafo_do_formalismo.adicionar_aresta(v1, v2, peso)

print("\nGrafo resultante (representação em lista de adjacência):")
grafo_do_formalismo.imprimir()

# Verificar se o grafo resultante é idêntico ao grafo_convertido anterior
print("\nVerificando se o grafo resultante é idêntico ao grafo convertido anteriormente...")
print(f"Mesmo número de vértices? {len(grafo_do_formalismo.vertices) == len(grafo_convertido.vertices)}")
print(f"Mesmo número de arestas? {sum(len(adj) for adj in grafo_do_formalismo.arestas.values()) // 2 == len(arestas)}")

# Visualizar o grafo
plt = grafo_do_formalismo.visualizar("Grafo construído a partir do formalismo G(V,(A,w))")
plt.show()