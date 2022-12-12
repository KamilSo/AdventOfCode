import copy
import numpy

Data = open('input.txt', 'rt')
Data = [x.replace('\n', '') for x in Data]
Data = [x.split(' ') for x in Data]
Tail = [[0, 0]]
Head = [[0, 0]]

def perform_moves():
    for moves in Data:
        Head_start = copy.deepcopy(Head[-1])
        for move_number in range(1,int(moves[1])+1):
            if moves[0] == 'U' :
                Head_start[1] +=1
            elif moves[0] == 'R':
                Head_start[0] += 1
            elif moves[0] == 'D':
                Head_start[1] -= 1
            elif moves[0] == 'L':
                Head_start[0] -= 1
            append_copy = copy.deepcopy(Head_start)
            Head.append(append_copy)

def sort_and_display():
    unique = []
    for coord in Tail:
        if coord not in unique:
            unique.append(coord)
    print(len(unique))

def Main():
    for Head_coord in Head:
        if Check_if_move(Head_coord,Tail[-1]):
            Tail.append(Calc_Tail(Head_coord,Tail[-1]))

def Calc_Tail(Head_pos,Tail_pos):
    Tail_new_pos = copy.deepcopy(Tail_pos)
    Coord_diff = [Head_pos[0] - Tail_pos[0], Head_pos[1] - Tail_pos[1]]
    if Coord_diff[0] != 0 and Coord_diff[1] == 0:
        Tail_new_pos[0] += numpy.sign(Coord_diff[0])
    elif Coord_diff[1] != 0 and Coord_diff[0] == 0:
        Tail_new_pos[1] += numpy.sign(Coord_diff[1])
    else:
        Tail_new_pos[0] += numpy.sign(Coord_diff[0])
        Tail_new_pos[1] += numpy.sign(Coord_diff[1])
    return Tail_new_pos

def Check_if_move(Head_pos,Tail_pos):
    Coord_diff = [abs(Head_pos[0]-Tail_pos[0]),abs(Head_pos[1]-Tail_pos[1])]
    return Coord_diff[0] > 1 or Coord_diff[1] > 1

perform_moves()
for n in range(9):
    Main()
    Head = Tail
    Tail = [[0,0]]
Tail = Head
print(Head)
print(Tail)
sort_and_display()
