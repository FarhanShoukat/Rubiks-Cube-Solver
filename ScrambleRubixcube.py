import numpy as np

xInitial = np.array([
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['R', 'R', 'R'],
        ['R', 'R', 'R'],
        ['R', 'R', 'R'],
        ['B', 'B', 'B'],
        ['B', 'B', 'B'],
        ['B', 'B', 'B'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y']
    ])


def FrontCW(x):  # action 1
    x[6:9, 0:3] = np.fliplr(x[6:9, 0:3].transpose())
    temp1 = np.array(x[2, 0:3])
    temp2 = np.array(x[9:12, 0])
    temp3 = np.array(x[15, 0:3])
    temp4 = np.array(x[3:6, 2])
    x[2, 0:3] = np.fliplr([temp4])[0]
    x[9:12, 0] = temp1
    x[15, 0:3] = np.fliplr([temp2])[0]
    x[3:6, 2] = temp3


def FrontACW(x):  # action 2
    FrontCW(x)
    FrontCW(x)
    FrontCW(x)


def UpCW(x):  # action 3
    x[0:3, 0:3] = np.fliplr(x[0:3, 0:3].transpose())
    temp1 = np.array(x[12, 0:3])
    temp2 = np.array(x[9, 0:3])
    temp3 = np.array(x[6, 0:3])
    temp4 = np.array(x[3, 0:3])
    x[12, 0:3] = temp4
    x[9, 0:3] = temp1
    x[6, 0:3] = temp2
    x[3, 0:3] = temp3


def UpACW(x):  # acion 4
    UpCW(x)
    UpCW(x)
    UpCW(x)


def DownCW(x):  # action 5 Front down clock wise
    x[15:18, 0:3] = np.fliplr(x[15:18, 0:3].transpose())
    temp1 = np.array(x[8, 0:3])
    temp2 = np.array(x[11, 0:3])
    temp3 = np.array(x[14, 0:3])
    temp4 = np.array(x[5, 0:3])
    x[8, 0:3] = temp4
    x[11, 0:3] = temp1
    x[14, 0:3] = temp2
    x[5, 0:3] = temp3


def DownACW(x):  # action 6
    DownCW(x)
    DownCW(x)
    DownCW(x)


def LeftCW(x):  # action 7

    x[3:6, 0:3] = np.fliplr(x[3:6, 0:3].transpose())
    temp1 = np.array(x[0:3, 0])
    temp2 = np.array(x[6:9, 0])
    temp3 = np.array(x[15:18, 0])
    temp4 = np.array(x[12:15, 2])
    x[0:3, 0] = np.fliplr([temp4])[0]
    x[6:9, 0] = temp1
    x[15:18, 0] = temp2
    x[12:15, 2] = np.fliplr([temp3])[0]


def LeftACW(x):  # action 8
    LeftCW(x)
    LeftCW(x)
    LeftCW(x)


def RightCW(x):  # action 9 Front right clock wise

    x[9:12, 0:3] = np.fliplr(x[9:12, 0:3].transpose())
    temp1 = np.array(x[0:3, 2])
    temp2 = np.array(x[12:15, 0])
    temp3 = np.array(x[15:18, 2])
    temp4 = np.array(x[6:9, 2])
    x[0:3, 2] = temp4
    x[12:15, 0] = np.fliplr([temp1])[0]
    x[15:18, 2] = np.fliplr([temp2])[0]
    x[6:9, 2] = temp3


def RightACW(x):  # action 10
    RightCW(x)
    RightCW(x)
    RightCW(x)


def BackCW(x):  # action 11 Front  back clock wise

    x[12:15, :] = np.fliplr(x[12:15, :].transpose())
    temp1 = np.array(x[0, 0:3])
    temp2 = np.array(x[3:6, 0])
    temp3 = np.array(x[17, 0:3])
    temp4 = np.array(x[9:12, 2])
    x[0, 0:3] = temp4
    x[3:6, 0] = np.fliplr([temp1])[0]
    x[17, 0:3] = temp2
    x[9:12, 2] = np.fliplr([temp3])[0]


def BackACW(x):  # action 12
    BackCW(x)
    BackCW(x)
    BackCW(x)


def PrintCube(x):
    print("             ", x[0, 0:3])
    print("             ", x[1, 0:3])
    print("             ", x[2, 0:3])
    print(x[3, 0:3], x[6, 0:3], x[9, 0:3], x[12, 0:3])
    print(x[4, 0:3], x[7, 0:3], x[10, 0:3], x[13, 0:3])
    print(x[5, 0:3], x[8, 0:3], x[11, 0:3], x[14, 0:3])
    print("             ", x[15, 0:3])
    print("             ", x[16, 0:3])
    print("             ", x[17, 0:3])


def make_move(x, move, reverse):
    # move number
    # reverse if 0 original move if 1 reverse of input move

    if reverse == 1:
        if move % 2 == 0:
            move = move - 1
        else:
            move = move + 1
    if move == 1:
        FrontCW(x)
        return "FrontCW"

    if move == 2:
        FrontACW(x)
        return "FrontACW"

    if move == 3:
        UpCW(x)
        return "UpCW"

    if move == 4:
        UpACW(x)
        return "UpACW"

    if move == 5:
        DownCW(x)
        return "DownCW"

    if move == 6:
        DownACW(x)
        return "DownACW"

    if move == 7:
        LeftCW(x)
        return "LeftCW"

    if move == 8:
        LeftACW(x)
        return "LeftACW"

    if move == 9:
        RightCW(x)
        return "RightCW"

    if move == 10:
        RightACW(x)
        return "RightACW"

    if move == 11:
        BackCW(x)
        return "BackCW"

    if move == 12:
        BackACW(x)
        return "BackACW"
