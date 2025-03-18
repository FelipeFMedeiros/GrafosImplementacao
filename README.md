# 📚 Implementação de Teoria dos Grafos 2025.1

Este repositório contém a implementação em Python de um grafo não direcionado e valorado, conforme especificado no trabalho prático da disciplina de Teoria dos Grafos da UERN, semestre 2025.1.

## 🎯 Objetivo

O objetivo deste trabalho é fixar o conteúdo básico e os procedimentos operacionais de um grafo não direcionado.

## 📝 Descrição

O projeto consiste na criação de uma estrutura de dados para representar um grafo G(V, (A, w)), onde:

-   V é o conjunto de vértices;
-   A é o conjunto de arestas;
-   w é o peso associado a cada aresta.

Além da estrutura de dados, foram implementadas rotinas para as seguintes funcionalidades:

1.  `g_form`: Receber o grafo pelo formalismo.
2.  `g_imprimir`: Imprimir a representação do grafo.
3.  `g_form_mAdj`: Converter formalismo em matriz de adjacência.
4.  `g_form_lAdj`: Converter formalismo em lista de adjacência.
5.  `g_form_mInc`: Converter formalismo em matriz de incidência.
6.  `g_mAdj_form`: Converter matriz de adjacência em formalismo.
7.  `g_mAdj_lAdj`: Converter matriz de adjacência em lista de adjacência.
8.  `g_mAdj_mInc`: Converter matriz de adjacência em matriz de incidência.
9.  `g_mInc_form`: Converter matriz de incidência em formalismo.
10. `g_mInc_mAdj`: Converter matriz de incidência em matriz de adjacência.
11. `g_mInc_lAdj`: Converter matriz de incidência em lista de adjacência.
12. `v_remover`: Remover um vértice.
13. `v_incluir`: Incluir um vértice.
14. `a_remover`: Remover uma aresta.
15. `a_incluir`: Incluir uma aresta.
16. `a_ehAdjacente`: Verificar se duas arestas são adjacentes.
17. `v_ehAdjacente`: Verificar se dois vértices são adjacentes.
18. `v_lAdj`: Imprimir a lista de adjacência de um vértice.
19. `a_lInc`: Imprimir os vértices incidentes de uma aresta.
20. `v_grau`: Imprimir o grau de um vértice.
21. `g_ehBipartido`: Verificar se o grafo é bipartido.
22. `g_ehCompleto`: Verificar se o grafo é completo.
23. `g_ehConexo`: Verificar se o grafo é conexo.
24. `g_ehMultigrafo`: Verificar se o grafo é multigrafo.
25. `g_ehRegular`: Verificar se o grafo é regular.

## ⚙️ Como usar

1.  Clone o repositório:

    ```bash
    git clone https://github.com/FelipeFMedeiros/GrafosImplementacao.git
    ```

2.  Navegue até o diretório do projeto:

    ```bash
    cd GrafosImplementacao
    ```

3.  Execute os scripts Python para testar as funcionalidades.

## 🧪 Critérios de Avaliação

-   Cada procedimento operacional será avaliado individualmente e valerá 0,2 pontos, se correto.
-   Será avaliada a estrutura de dados usada para representação do grafo.
-   Será avaliado o conteúdo abordado em sala de aula: formalismo, matriz de adjacência, lista de adjacência, matriz de incidência, classificação de grafos específicos (conexo, completo, multigrafo, bipartido, regular).
-   Serão avaliadas a colaboração entre o grupo e a capacidade (dos componentes) de explicar/demonstrar o código diante de um questionamento, se houver.
-   Será avaliada a clareza dos comentários no código.
-   Será avaliada a entrega do código-fonte no prazo estabelecido.

## 📅 Prazo de Entrega

18/03/2025

## 🧑‍🏫 Professor

Rosiery Maia

## 🤝 Contribuidores

-   [Felipe Medeiros](https://github.com/FelipeFMedeiros)
-   [Ismael Santos](https://github.com/ismaelsantos1)
-   [Mateus Garcia](https://github.com/M2004GV)
-   [Nicolas Macedo](https://github.com/nicmacedo)
