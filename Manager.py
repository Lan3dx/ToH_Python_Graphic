def Generate(elements = 3):
    tower = []
    for i in range(elements):
        tower.append([])
        for _ in range(3): 
            tower[len(tower)-1].append(" ")
    for i in range(elements,0,-1): tower[i-1][0] = i
    return tower
def find(tower, symbol):
    for i in range(len(tower)):
        for j in range(3):
            if tower[i][j] == symbol: return i, j
def Win(tower):
    for m in range(2):
        for i in range(len(tower)):
            if tower[i][m] != " ": return False
    return True
def upper(tower, j):
    for i in range(len(tower)):
        if tower[i][j] != " ":return tower[i][j]
def equals(tower):
    if Win(tower) == True: exit()
    upperpoints = [0,0,0]
    for i in range(3): upperpoints[i] = upper(tower,i)
    if None in upperpoints: upperpoints[upperpoints.index(None)] = 0
    upperpoints.sort()
    if upperpoints[1] == 1: return find(tower,upperpoints[2])
    else: return find(tower,upperpoints[1])