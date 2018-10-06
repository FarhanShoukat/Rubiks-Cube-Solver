from ScrambleRubixcube import xInitial, make_move
import numpy as np
import sqlite3
from sqlite3 import Error


class St:
    cube = None
    cost = 0


def get_corner_string(cube):
    string = ''
    for i in range(18):
        if i % 3 == 0 or i % 3 == 2:
            string = string + cube[i, 0] + cube[i, 2]
    return string


###################################################


db = dict()
front = list()
goal = St()
goal.cube = np.array(xInitial)
front.append(goal)
db[get_corner_string(goal.cube)] = 0
# cost = 0
while len(front) != 0:
    curr = front.pop(0)
    if curr.cost < 5:
        child_cost = curr.cost + 1
        for i in range(12):
            new = St()
            new.cube = np.array(curr.cube)
            new.cost = child_cost
            make_move(new.cube, i + 1, 0)
            # if cost < child_cost:
            #    cost = child_cost
            #    print(cost)
            string = get_corner_string(new.cube)
            if string not in db.keys():
                db[string] = new.cost
                front.append(new)

try:
    cube = goal.cube

    conn = sqlite3.connect('corners.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE CornerValue(Corners VARCHAR, Value INT)')
    print(sqlite3.version)
    cursor.executemany('INSERT INTO CornerValue(Corners, Value) VALUES (?, ?)', db.items())
    conn.commit()
except Error as e:
    print(e, 'error occurred')
finally:
    cursor.close()
    conn.close()
