input = open('input.txt','rt')
input = input.readlines()
stacks = input[:8]
stack_number = input[8:9]
moves = input[10:]
stack_index=[]
'''stacks = input[:3]
stack_number = input[3:4]
moves = input[5:]'''

for stack_nr in stack_number:
    for n in range(len(stack_nr)):
        try:
            if int(stack_nr[n]) in range(10):
                stack_index.append(int(n))
            else:
                pass
        except:
            pass

for index_nr in stack_index:
    stack_name = 'stack' + str(stack_nr[index_nr])
    globals()[str(stack_name)] = []

for stack in stacks:
    for index_nr in stack_index:
        x= stack[int(index_nr)]
        stack_name = 'stack' + str(stack_nr[index_nr])
        if x in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            globals()[str(stack_name)].append(x)
        else:
            pass

for index_nr in stack_index:
    stack_name = 'stack' + str(stack_nr[index_nr])
    globals()[str(stack_name)].reverse()

for x in range(10): #this is just to check if code before works (It does work) xD
    try:
        stack_name = 'stack' + str(x)
        print(globals()[str(stack_name)])
    except:
        pass

for move in moves: #something probably wrong below here
    try:
        for n in range(int(move[5])):
            stack_name = 'stack' + str(move[12])
            crate_to_move = globals()[stack_name].pop(-1)
            stack_name = 'stack' + str(move[17])
            globals()[stack_name].append(crate_to_move)
    except:
        x = move[5:7]
        for n in range(int(x)):
            stack_name = 'stack' + str(move[13])
            crate_to_move = globals()[stack_name].pop(-1)
            stack_name = 'stack' + str(move[18])
            globals()[stack_name].append(crate_to_move)

for n in range(10):
    try:
        stack_name = 'stack'+str(n)
        print(globals()[stack_name][-1])

    except:
        pass
