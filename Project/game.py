
def Bord(xState, yState):
    one = 'X' if xState[0] else ('O' if yState[0] else 1)
    two = 'X' if xState[1] else ('O' if yState[1] else 2)
    three = 'X' if xState[2] else ('O' if yState[2] else 3)
    four = 'X' if xState[3] else ('O' if yState[3] else 4)
    five = 'X' if xState[4] else ('O' if yState[4] else 5)
    six = 'X' if xState[5] else ('O' if yState[5] else 6)
    seven = 'X' if xState[6] else ('O' if yState[6] else 7)
    eight = 'X' if xState[7] else ('O' if yState[7] else 8)
    nine = 'X' if xState[8] else ('O' if yState[8] else 9)
    print(f" {one} | {two} | {three}")
    print(f"---|---|---")
    print(f" {four} | {five} | {six}")
    print(f"---|---|---")
    print(f" {seven} | {eight} | {nine} ")


def sum(x, y, z):
    return x+y+z


def checkWin(xState, yState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print(f"{user} Is Win")
            return 1
        elif(sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3):
            print(f"{user2} is win")
            return 0
    return-1


xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
trun = 1
print("Welcome Python Game")
user = input("Enter User One Name : ")
user2 = input("Enter User Two Name : ")
while (True):
    Bord(xState, yState)
    if(trun == 1):
        print(f"{user}'s Trun : ")
        index = int(input("Please enter index of box : "))
        xState[index-1] = 1
    else:
        print(f"{user2}'s Trun : ")
        index = int(input("Please enter index of box : "))
        yState[index-1] = 1
    win = checkWin(xState, yState)
    if(win != -1):
        print("Game Over")
        break
    trun = 1-trun
