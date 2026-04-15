from collections import deque

# branco = 0
# cinza  = 1
# preto  = 2

class vertice:
    def __init__(self, nome):
        self.nome=nome
        self.d = 0
        self.f = 0
        self.p = None
        self.cor=0

    def print_v(self):
        print(self.nome)

def ordenacao_topologica(grafo):
    tempos = []
    tempo=0
    for u in grafo:
        if u.cor == 0:
            dfs_visit(grafo, u, tempo, tempos)
    return tempos

def dfs_visit(grafo, u, tempo, tempos):
    tempo+=1
    u.d=tempo
    u.cor=1
    for v in grafo[u]:
        if v.cor==0:
            dfs_visit(grafo, v, tempo, tempos)
    u.cor=2
    tempo+=1
    u.f=tempo
    tempos.append((u.nome, u.f))

a = vertice('a')
b = vertice('b')
c = vertice('c')
d = vertice('d')
e = vertice('e')
f = vertice('f')


grafo = {
    a:[d, f],
    b:[e],
    c:[e, f],
    d:[a],
    e:[b, c, f],
    f:[c, e]
}

tempos = ordenacao_topologica(grafo)

tempos = sorted(tempos, key=lambda x: x[1], reverse=True)
print(tempos)
