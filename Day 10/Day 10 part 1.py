Data = open('input.txt','rt')
Data = [x.replace('\n','') for x in Data]
Data = [x.replace('noop','n') for x in Data]
Data = [x.replace('addx','a') for x in Data]
Data = [x.split(' ') for x in Data]
Cycle = 1
Register = 1
Signal_s = []

def check_defined_cycles():
    if Cycle in range(20,221,40):
        Signal_s.append(Cycle * Register)

def Sum_items():
    sum = 0
    for signal in Signal_s:
        sum += signal
    print(sum)

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
Sum_items()

