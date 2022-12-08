string = open('input.txt','rt')
lines = string.readlines()
All_lines = ''

for line in lines:
    All_lines += str(line)

def check_duplicate(list):
    if len(list) == len(set(list)):
        return False
    else:
        return True

def marker(string):
    for n in range(len(string)):
        packet_range = []
        for i in range(14):
                packet_range.append((string[i+n]))
        duplicate = check_duplicate(packet_range)
        if duplicate == True:
            pass
        else:
            print(n+14)
            break

marker(All_lines)