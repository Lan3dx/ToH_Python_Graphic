def std(steps, tower):
    print("\n\n   [ ",steps," ]    ",end="\n")
    for i in range(len(tower)):
        for j in range(3):
            print("| ",end="")
            print(tower[i][j],end=" ")
        print("|")