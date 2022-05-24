# Import
import Manager
import Render
import Compute
import Transpose

# Configurate
def build():

    sNum = int(input(">>  amount of elements:  "))

    if sNum > 9:
         print("the",str(sNum),"disk tower of Hanoi problem can be solved in",'{0:,}'.format((2**sNum)-1).replace(',', ' '),"steps")
         build()

    tower = (Manager.Generate(sNum))
    steps = 0

    start(steps,tower)

# Begin
def start(steps,tower):

    Render.std(steps, tower)

    while True:

        if Manager.Win(tower) == True:
            False
            exit()

        n, j = Manager.find(tower, 1)
        metavar = 0
        for i in range(len(tower)):
            if tower[i][j] != " ": metavar += 1

        match metavar % 2:
            case 0:
                match j:
                    case 0: 
                        steps = Compute.Even.Left(tower, steps)
                    case 1: 
                        steps = Compute.Even.Center(tower, steps)
                    case 2: 
                        steps = Compute.Even.Right(tower, steps)
            case _:
                match j:
                    case 0: 
                        steps = Compute.NotEven.Left(tower, steps)
                    case 1: 
                        steps = Compute.NotEven.Center(tower, steps)
                    case 2: 
                        steps = Compute.NotEven.Right(tower, steps)

        Transpose.OtherElement(tower)
        steps += 1
        Render.std(steps, tower)
build()