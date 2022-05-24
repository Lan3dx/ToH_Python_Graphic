import Manager

def OtherElement(tower):
    onex, oney = Manager.find(tower,1)
    f_x, f_y = Manager.equals(tower)
    for i in range(3):
        if i != f_y and i != oney:
            match i:
                case 0: Left(tower, tower[f_x][f_y])
                case 1: Center(tower, tower[f_x][f_y])
                case 2: Right(tower, tower[f_x][f_y])
def Left(tower, symbol):
    f_X, f_Y = Manager.find(tower, symbol)
    tower[f_X][f_Y] = " "
    for i in range(len(tower)):
        if tower[i][0] != " ": 
            tower[i-1][0] = symbol
            return
    else: tower[len(tower)-1][0] = symbol
def Center(tower, symbol):
    f_X, f_Y = Manager.find(tower, symbol)
    tower[f_X][f_Y] = " "
    for i in range(len(tower)):
        if tower[i][1] != " ": 
            tower[i-1][1] = symbol
            return
    else: tower[len(tower)-1][1] = symbol
def Right(tower, symbol):
    f_X, f_Y = Manager.find(tower, symbol)
    tower[f_X][f_Y] = " "
    for i in range(len(tower)):
        if tower[i][2] != " ": 
            tower[i-1][2] = symbol
            return
    else: tower[len(tower)-1][2] = symbol