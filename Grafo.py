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
        v1, u1 = a1 #Primeira aresta (v1--u1)
        v2, u2 = a2 #Segunda aresta (v2--u2)
        return v1 in (v2,u2) or u1 in (v2,u2)

    def v_eh_adjacente(self, v1, v2):
        return any(v2 == vizinho for vizinho, _ in self.arestas.get(v1, []))


    def lista_adjacencia(self, v):
        return self.arestas.get(v, [])

    def grau(self, v):
        return len(self.arestas.get(v, []))

    def eh_regular(self):
        grau_ini = self.grau(next(iter(self.vertices)))  # salva o grau do primeiro vértice do grafo
        for v in self.vertices:  # verifica o grau do resto dos vértices do grafo
            if self.grau(v) != grau_ini:  # compara se os outros graus com o do primeiro
                return False  # retorna False se algum grau for diferente
        return True  # retorna True se todos os graus forem iguais

# Exemplo de uso
g = Grafo()
g.adicionar_vertice(1)
g.adicionar_vertice(2)
g.adicionar_vertice(3)
g.adicionar_aresta(1, 2, 5)
g.adicionar_aresta(2, 3, 7)
g.imprimir()

print(g.a_eh_Adjacente((1, 2), (2, 3)))  # True
print(g.a_eh_Adjacente((1, 2), (3, 4)))  # False
print(g.v_eh_adjacente(1,2))
print("Grau do vértice 2:", g.grau(2))
print('Lista de de Adjacência de um vertíce: ', g.lista_adjacencia(1))