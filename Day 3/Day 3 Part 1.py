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

for Rugsack in Rugsacks:
    Compartment_size = int(len(Rugsack)/2)
    Compartment_1 = Rugsack[0:Compartment_size]
    Compartment_2 = Rugsack[Compartment_size:]
    stop = False
    while stop == False:
        for i in range(Compartment_size):
            Item_1 = Compartment_1[i]
            for j in range(Compartment_size):
                Item_2 = Compartment_2[j]
                if Item_2 == Item_1:
                    sum = sum + AddPriority(Item_1)
                    stop = True
                    break
                else:
                    pass
            if stop == True:
                break

print(sum)

