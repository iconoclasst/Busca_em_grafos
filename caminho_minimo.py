from collections import deque

class vertice:
    def __init__(self, nome):
        self.nome=nome
        self.d=0
        self.cor=0
        self.p=None

def bfs(grafo, s, d):
    s.cor=1
    fila = deque([s])
    while fila:
        u = fila.popleft()
        for v in grafo[u]:
            if v.cor==0:
                v.p = u
                v.cor=1
                v.d = u.d+1
                fila.append(v)
                if v.nome == d.nome:
                    caminho = []
                    atual = v
                    while atual.p is not None:
                        caminho.append((atual.p.nome, atual.nome))
                        atual = atual.p
                    caminho.reverse()
                    return caminho, v.d
    return 1, 1

a = vertice('a')
b = vertice('b')
c = vertice('c')
d = vertice('d')
e = vertice('e')
f = vertice('f')

G = {
a: [b, c],
b: [a, d, e],
c: [a, f],
d: [b],
e: [b, f],
f: [c, e]
}

source = a
dest = e


caminho, distancia = bfs(G, source, dest)
print(f"Para ir de {source.nome} até {dest.nome}, usa as arestas {caminho} de distancia {distancia}")