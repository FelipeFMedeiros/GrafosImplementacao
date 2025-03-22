from Grafo import Grafo
import matplotlib.pyplot as plt
"""
BHO -> 000          ORI -> 777
BRA -> 111          POA -> 888
CBA -> 222          REC -> 999
CTB -> 333          RIO -> 1000
FOR -> 444          SAL -> 1001
MAN -> 555          SPO -> 1002
NAT -> 666          TES -> 10003
"""

# Criar grafo de exemplo
g = Grafo()

# Adicionar vértices
#for i in range(1, 7):
#    g.adicionar_vertice(i)

# Adicionar arestas com pesos
#g.adicionar_aresta(1, 2, 5)
#g.adicionar_aresta(1, 3, 3)
#g.adicionar_aresta(2, 3, 1)
#g.adicionar_aresta(2, 4, 7)
#g.adicionar_aresta(3, 5, 2)
#g.adicionar_aresta(4, 5, 4)
#g.adicionar_aresta(4, 6, 6)
#g.adicionar_aresta(5, 6, 8)
vertices = [000, 111, 222, 333, 444, 555, 666, 777, 888, 999, 1000, 1001, 1002]
arestas = [
    (111, 000, 716),
    (222,000 , 1594),
    (333, 000, 1004),
    (444, 000, 2528),
    (555, 000, 3951),
    (666, 000, 2348),
    (777, 000, 9001),
    (888, 000, 1712),
    (999, 000, 2061),
    (1000, 000, 439),
    (1001, 000, 1372),
    (1002, 000, 586),
    #Col 2
    (222, 111, 1133),
    (333, 111, 1366),
    (444, 111, 2200),
    (555, 111, 3490),
    (666, 111, 2422),
    (777, 111, 9002),
    (888, 111, 2027),
    (999, 111, 2135),
    (1000, 111, 1148),
    (1001, 111, 1446),
    (1002, 111, 1015),
    #Col 3
    (333, 222, 1679),
    (444, 222, 3406),
    (555, 222, 2357),
    (666, 222, 3543),
    (777, 222, 9003),
    (888, 222, 2206),
    (999, 222, 3255),
    (1000, 222, 2017),
    (1001, 222, 2566),
    (1002, 222, 1614),
    #Col 4
    (444, 333, 3541),
    (555, 333, 4036),
    (666, 333, 3365),
    (777, 333, 9004),
    (888, 333, 711),
    (999, 333, 3231),
    (1000, 333, 852),
    (1001, 333, 2566),
    (1002, 333, 1614),
    #Col 5
    (555, 444, 5763),
    (666, 444, 537),
    (777, 444, 9005),
    (888, 444, 4242),
    (999, 444, 800),
    (1000, 444, 2826),
    (1001, 444, 1389),
    (1002, 444, 3127),
    #Col 6
    (666, 555, 5985),
    (777, 555, 9006),
    (888, 555, 4563),
    (999, 555, 5698),
    (1000, 555, 4374),
    (1001, 555, 5009),
    (1002, 555, 3971),
    #Col 6
    (777, 666, 9007),
    (888, 666, 4066),
    (999, 666, 298),
    (1000, 666, 2625),
    (1001, 666, 1131),
    (1002, 666, 2947),
    #Col 7
    (888, 777, 9008),
    (999, 777, 9009),
    (1000, 777, 9010),
    (1001, 777, 9011),
    (1002, 777, 9012),
    #Col 8
    (999, 888, 3779),
    (1000, 888, 1553),
    (1001, 888, 3090),
    (1002, 888, 1109),
    #Col 9
    (1000, 999, 2338),
    (1001, 999, 897),
    (1002, 999, 2660),
    #Col 10
    (1001, 1000, 1678),
    (1002, 1000, 429),
    #Col 11
    (1002, 1001, 1962)
           ]

#Todas as arestas e vertices foram inseridos. O que precisar ser retirado, será.

#Informando o formalismo

print(f'O formalismo do Grafo é:\n{g.g_form(vertices, arestas)}')

#Representando o gráfico
g.vertices = set(vertices)
print("Representação do grafo:")
g.imprimir()

#Removendo a aresta (FOR, ORI)
#g.remover_aresta(777, 444)

#Adicionando o vértice TES
#g.adicionar_vertice(1003)

#Removendo o vértice TES E ORI
g.remover_vertice(1003), g.remover_vertice(444) # type: ignore

print(f"Pela representação, verifique se SPO é adjacente a NAT:\n{g.v_eh_adjacente(1002, 666)}")
#Imprima a lista de adjacência do vértice NAT
print(f'\n{g.lista_adjacencia(666)}\n\n')

print(f'Trata-se de um grafo completo?\n{g.eh_completo()}')
print(f'Trata-se de um multigrafo?\n{g.eh_multi()}')
print(f'Trata-se de um grafo bipartido?\n{g.eh_bipartido()}')
print(f'Trata-se de um grafo conexo?\n{g.eh_conexo()}')
print(f'Trata-se de um grafo regular?\n{g.eh_regular()}')
print(f'Informe o grau do vértice NAT:\n{g.grau(666)}')
print(f'Informe a representação do grafo por Matriz de Adjacência:\n{g.g_form_mAdj()}')
print(f'Informe a representação do grafo por Lista de Adjacência:\n{g.g_form_lAdj(vertices, arestas)}')
print(f'Informe a representação do grafo por Matriz de Incidência:\n{g.g_form_mInc(vertices, arestas)}')


# Verificações de propriedades do grafo
print("\nPropriedades do grafo:")
print("O grafo é completo?", g.eh_completo())
print("O grafo tem arestas múltiplas?", g.eh_multi())
print("O grafo atual é bipartido?", g.eh_bipartido())
print("O grafo agora é conexo?", g.eh_conexo())
print("O grafo é regular?", g.eh_regular())

# Verificando o grau do vértice NAT (666)
print(f"\nO grau do vértice NAT (666) é: {g.grau(666)}")

#Visualizando o grafo
g.visualizar()
plt.show()
