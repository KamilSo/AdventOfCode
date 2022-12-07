data = open('input.txt','r')
data = [x.replace('\n','') for x in data]
commands = []
directory_items = {}

def create_keys():
    for item in data:
        if item[0:3] == 'dir' and item[0:3] not in directory_items:
            directory_items[item[:]] = None
        else:
            pass

def append_commands():
    for index,item in enumerate(data,start=0):
        if item[0] == '$':
            commands.append(item)
        else:
            pass

def append_data():
    pointer = 0
    for command_index, command in enumerate(commands):
        items = []
        if data[command_index] == command:
            pass
        elif data[command_index+pointer][:3] == 'dir' and data[command_index+pointer+1][:3] != 'dir':
            if directory_items[data[command_index+pointer]] == None:
                items = []
            else:
                items.append(directory_items[data[command_index+pointer]])
            while data[command_index+pointer+1][:3] != 'dir':
                item = data[command_index+pointer+1].replace('.', ' ').split(' ')
                items.append(item[0])
                pointer += 1
                if data[command_index+pointer+1][:3] == 'dir' or data[command_index+pointer+1][0] == '$':
                    directory_items[data[command_index]] = items
                    break


create_keys()
append_commands()
append_data()
print(directory_items)
print(data)
print(commands)
