import random

def generer_grille(n, obstacles):
    grille = [[0] * n for _ in range(n)]
    for _ in range(obstacles):
        x, y = random.randrange(n), random.randrange(n)
        grille[x][y] = 1
    return grille

def afficher(grille):
    for ligne in grille:
        print(' '.join('██' if c else '··' for c in ligne))
        

def chemin(grille, depart, arrivee):
    n = len(grille)
    file, visites = [(depart, [depart])], {depart}
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while file:
        (x,y), route = file.pop(0)
        if (x,y) == arrivee: return route
        for dx,dy in directions:
            nx,ny = x+dx, y+dy; v = (nx,ny)
            if 0<=nx<n and 0<=ny<n and grille[nx][ny]==0 and v not in visites:
                visites.add(v); file.append((v, route+[v]))
    return None

if __name__ == '__main__':
    g = generer_grille(8, 10); debut, fin = (0,0), (7,7)