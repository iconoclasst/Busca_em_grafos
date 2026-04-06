# README

## BFS (Breadth-First Search)

A busca em largura percorre o grafo em níveis, visitando primeiro os vizinhos mais próximos. Utiliza uma fila (FIFO) e marca os vértices para evitar revisitas.

Cada vértice possui:
- `cor`: estado (branco, cinza, preto)
- `d`: distância até a origem
- `pre`: predecessor

## Grafo utilizado

Representação por lista de adjacência:  
a -> d, f  
b -> e  
c -> e, f  
d -> a  
e -> b, c, f  
f -> c, e  


## Saída da BFS (origem: a)

Arestas da árvore gerada:  
(a, d), (a, f), (f, c), (f, e), (e, b)  
