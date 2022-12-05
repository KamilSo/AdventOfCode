Ids = open('ID.txt','rt')
Ids = Ids.readlines()
sum = 0

def identify_range(Id):
    first_found = False
    second_found = False
    fourth_found = False
    for n in range(len(Id)):
        check = Id[n]
        if check == '-' and not first_found:
            first = int(Id[0:n])
            first_pos = n
            first_found = True
        elif check == ',' and not second_found and first_found:
            second = int(Id[first_pos+1:n])
            second_pos = n
            second_found = True
        elif check == '-' and second_found:
            third = int(Id[second_pos+1:n])
            third_pos = n
        elif check == '\n' and not fourth_found:
            fourth = int(Id[third_pos+1:-1])
            fourth_found = True
        else:
            pass
    return first,second,third,fourth

for Id in Ids:
    Elf_1 = []
    Elf_2 = []
    if Id[-1] != '\n':
        Id = Id + '\n'
    range_Id = identify_range(Id)
    for n in range(range_Id[0],range_Id[1]+1):
        Elf_1.append(n)
    for n in range(range_Id[2],range_Id[3]+1):
        Elf_2.append(n)
    try:
        Overlap_found = False
        for task in Elf_1:
            if not Overlap_found:
                for n in range(len(Elf_2)):
                    if task == Elf_2[n] and not Overlap_found:
                        sum+=1
                        Overlap_found= True
        for task in Elf_2:
            if not Overlap_found:
                for n in range(len(Elf_1)):
                    if task == Elf_1[n] and not Overlap_found:
                        sum+=1
                        Overlap_found= True
    except:
        pass

print(sum)
