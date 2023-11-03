from grafo import *

g = Grafo()
g.CriandoNo("Samyla")
g.CriandoVizinhos("Alex", "Talia", 5)
g.CriandoVizinhos("Carol", "Alex", 1)
g.CriandoVizinhos("Samyla", "Talia", 4)
g.CriandoVizinhos("Talia", "Alex", 9)

print(g.grafo)