Data = open('input.txt','rt')
def parse(data): #[monkeyname,items,operation,check,outcome if true,outcome if false]
    data = [x.replace(' ','').replace('Startingitems:', '').replace('Operation:new=old', '').replace('\n', '').replace
            ('Test:divisibleby', '').replace('Iftrue:throwto','').replace('Iffalse:throwto','').replace(':','') for x in data]
    parsed_data = []
    for index,data_item in enumerate(data):
        if data_item[0:6] == 'Monkey':
            pointer = 0
            globals()[data_item] = []
            while data[pointer] != '':
                globals()[data_item].append(data[index+pointer])
                pointer+=1
            parsed_data.append(globals()[data_item])
        else:
            continue
    for index,data_item_2 in enumerate(parsed_data):  # puts monkey items in a list data type
        monkey = data_item_2[0]
        item_append = []
        for item in data_item_2[1].split(','):
            item_append.append(item)
        del globals()[monkey][1]
        globals()[monkey].insert(1, item_append)
        parsed_data[index].append(0)
    return parsed_data

def Main(data):
        for data_index,data_item in enumerate(data):
            check = int(data_item[3])
            for item_index, item in enumerate(data_item[1]):
                worry_lvl = int(item)
                operation = data_item[2][0]
                value = data_item[2][1:]
                if operation == '+':
                    if value == 'old':
                        worry_lvl+=worry_lvl
                    else:
                        worry_lvl+=int(value)
                elif operation == '*':
                    if value == 'old':
                        worry_lvl*=worry_lvl
                    else:
                        worry_lvl*=int(value)
                worry_lvl = int(worry_lvl)//3
                if worry_lvl%check == 0:
                    data[int(data_item[4][-1])][1].append(worry_lvl)
                    data[data_index][-1] +=1
                else:
                    data[int(data_item[5][-1])][1].append(worry_lvl)
                    data[data_index][-1] +=1
            data[data_index][1] = []
def bubsort_and_display(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    sum = list[-1]*list[-2]
    print(sum)
Data = parse(Data)
for round in range(20):
    Main(Data)
item_sums = []
for item in Data:
    item_sums.append(item[-1])
bubsort_and_display(item_sums)


