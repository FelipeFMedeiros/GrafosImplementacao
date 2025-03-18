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