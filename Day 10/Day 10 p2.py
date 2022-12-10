import math
Data = open('input.txt','rt')
Data = [x.replace('\n','') for x in Data]
Data = [x.replace('noop','n') for x in Data]
Data = [x.replace('addx','a') for x in Data]
Data = [x.split(' ') for x in Data]
Cycle = 1
Register = 1
Signal_s = []
Crt_display = []

def check_defined_cycles():
    if Cycle in range(0,240):
        pixel_pos = [Register-1,Register,Register+1]
        Crt_draw_pos = Cycle-1
        for pixel in pixel_pos:
            if Crt_draw_pos%40 == pixel:
                Crt_display[math.ceil(Cycle /40) - 1][pixel] = '#'

def display_letters():
    for row in Crt_display:
        for elemt in row:
            print(elemt,end='')
        print('\n',end='')

for n in range(6):
    Row = []
    for n in range(40):
        Row.append('.')
    Crt_display.append(Row)

for instruction in Data:
    if instruction[0] == 'n':
        Cycle+=1
        check_defined_cycles()
    elif instruction[0] == 'a':
        for x in range(2):
            Cycle+=1
            if x == 1:
                Register += int(instruction[1])
                check_defined_cycles()
                continue
            else:
                check_defined_cycles()
display_letters()