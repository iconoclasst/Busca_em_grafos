from collections import deque

class vertice:
    def __init__(self, nome):
        self.nome=nome
        self.cor=0
        self.p=None
        self.d=0
        self.flag=None

def bfs(grafo, s):
    fila = deque([s])
    s.flag=0

    while fila:
        u = fila.popleft()
        # print(f"U: {u.nome}, flag: {u.flag}")
        for v in grafo[u]:
            if v.flag is None:
                # print(f"V: {v.nome}, flag: {v.flag}")
                v.flag= 1 - u.flag
                v.d=u.d+1
                v.p=u
                fila.append(v)
            elif v.flag == u.flag:
                return False
    return True

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

# bfs(G, a)

print("É bipartido" if bfs(G, a) else "Não é bipartido")