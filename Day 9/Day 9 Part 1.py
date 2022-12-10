import copy

Data = open('input.txt','rt')
Data = [x.replace('\n','') for x in Data]
Data = [x.split(' ') for x in Data]
Tail = [[0,0]]
Head = [[0,0]]
def perform_moves():
    for index,moves in enumerate(Data):
        Head_start = copy.deepcopy(Head[-1])
        for move_number in range(1,int(moves[1])+1):
            if moves[0] == 'U' :
                Head_start[1] +=1
            elif moves[0] == 'R':
                Head_start[0] +=1
            elif moves[0] == 'D':
                Head_start[1] -= 1
            elif moves[0] == 'L':
                Head_start[0] -=1
            append_copy = copy.deepcopy(Head_start)
            Head.append(append_copy)

def Tail_range_fun():
    Tail_rg = []
    Coord = Tail[-1]
    Tail_rg.append([Coord[0] + 1,Coord[1] - 1])
    Tail_rg.append([Coord[0] - 1, Coord[1] + 1])
    Tail_rg.append([Coord[0] - 1, Coord[1] - 1])
    Tail_rg.append([Coord[0] + 1, Coord[1] + 1])
    return Tail_rg

def Check_corner_dulplicate():
    Tail_range = [[1,1],[1,0],[0,0],[0,1]]
    for index,Coords in enumerate(Head):
        if index == 0:
            continue
        elif index == len(Head)-1:
            break
        else:
            Tail_coords = Tail[-1]
            Head_next_move = Head[index + 1]
            Coord_diff = [abs(Head_next_move[0] - Tail_coords[0]), abs(Head_next_move[1] - Tail_coords[1])]
            if Coord_diff not in Tail_range:
                Tail_append = Coords
        try:
            Tail.append(Tail_append)
        except:
            pass

def sort_and_display():
    unique = []
    for coord in Tail:
        if coord not in unique:
            unique.append(coord)
    print(unique)
    print(len(unique))

perform_moves()
Check_corner_dulplicate()
sort_and_display()

