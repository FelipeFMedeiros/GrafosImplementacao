from Grafo import Grafo
import matplotlib.pyplot as plt

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

# Testar se o grafo é completo
print("\nVerificando se o grafo é completo:")
print("O grafo atual é completo?", g.eh_completo())

# Testar a função a_lInc
print("\nVértices incidentes à aresta (1, 2):", g.a_lInc((1, 2)))
print("Vértices incidentes à aresta (1, 3):", g.a_lInc((1, 3)))

print("\nLista de adjacência do vértice 1:", g.lista_adjacencia(1))

# Visualizar o grafo
plt = g.visualizar("Grafo com múltiplas arestas")
plt.show()