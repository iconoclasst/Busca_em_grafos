from collections import deque

grafo = {
    'a':['d', 'e'],
    'b':['d', 'f', 'c'],
    'c':['b', 'f'],
    'd':['a', 'b'],
    'e':['a'],
    'f':['b', 'c', 'g'],
    'g':['f']
}

def bfs(grafo, start):
    visitados = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visitados:
            visitados.append(node)
            print(node, end=" ")

            for n in grafo[node]:
                if n not in visitados:
                    queue.append(n)

bfs(grafo, 'a')