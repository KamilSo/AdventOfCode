Rugsacks = open('Rugsacks.txt','rt')
Rugsacks = Rugsacks.readlines()
sum = 0
def AddPriority(Item):
    LowerCase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if Item in LowerCase:
        priority = LowerCase.index(Item)+1
    else:
        priority = LowerCase.index(Item.lower())+27
    return priority

for n in range(0,len(Rugsacks),3):
    Elf_1= Rugsacks[n]
    Elf_2 = Rugsacks[n+1]
    Elf_3 = Rugsacks[n+2]
    stop=False
    while stop == False:
        for i in range(len(Elf_1)):
            Item_1 = Elf_1[i]
            for j in range(len(Elf_2)):
                Item_2 = Elf_2[j]
                for k in range(len(Elf_3)):
                    Item_3 = Elf_3[k]
                    if Item_2 == Item_1 and Item_3 == Item_1 and Item_3 == Item_2:
                        sum = sum + AddPriority(Item_1)
                        stop = True
                        break
                    elif Item_1 == Elf_1[-1]:
                        stop = True
                        break
                    else:
                        pass
                if stop == True:
                    break
            if stop == True:
                break

print(sum)

