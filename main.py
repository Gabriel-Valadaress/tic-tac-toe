positions = {"1": "-",
             "2": "-",
             "3": "-",
             "4": "-",
             "5": "-",
             "6": "-",
             "7": "-",
             "8": "-",
             "9": "-",           
}

positionsAvaliable = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def currentPositionPrint():
    return ("""
    Current positions:
    {} | {} | {}
    {} | {} | {}
    {} | {} | {}
""".format(
    positions["1"], positions["2"], positions["3"],
    positions["4"], positions["5"], positions["6"],
    positions["7"], positions["8"], positions["9"]
))

positionNumber = (f"""
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9 
""")

def verifyWinner(positions):
    winning_combinations = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["1", "4", "7"],
        ["2", "5", "8"],
        ["3", "6", "9"],
        ["1", "5", "9"],
        ["3", "5", "7"]
    ]

    for i in range(len(winning_combinations)):
        for j in range(3):
            winning_combinations[i][j] = positions[winning_combinations[i][j]]
        if winning_combinations[i].count("X") == 3:
            return "Cross Wins"
        elif winning_combinations[i].count("O") == 3:
            return "Circle Wins"
    return None
            
i = 1
while i <= 9:
    if i == 1:
        print(currentPositionPrint())
    x = 0
    if i % 2 != 0:
        while x == 0:
            print(positionNumber)
            userPosition = input("Cross turn - Type the position: ")
            if userPosition in positionsAvaliable:
                positionsAvaliable.remove(userPosition)
                positions[userPosition] = "X"
                x += 1
            else:
                print("Not a valid position.")
    else:
        while x == 0:
            print(positionNumber)
            userPosition = input("Circle turn - Type the position: ")
            if userPosition in positionsAvaliable:
                positionsAvaliable.remove(userPosition)
                positions[userPosition] = "O"
                x += 1
            else:
                print("Not a valid position.")
    i += 1
    print(currentPositionPrint())
    if verifyWinner(positions) != None:
        print(verifyWinner(positions))
        quit()
    elif i == 10:
        print("Draw")
