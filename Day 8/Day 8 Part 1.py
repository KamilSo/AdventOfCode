data = open('input.txt','rt')
data = [x.replace('\n','') for x in data]

def format_row_column():
    formated_data =[]
    for index, trees in enumerate(data):
        row = []
        row.append(trees)
        temp = []
        for n in range(len(row[0])):
            temp.append(int(row[0][n]))
        formated_data.append(temp)
    return formated_data

def checkbottom(tree_input,index_input,tree_index):
    visible = False
    for n in range(index_input+1,len(data)):
        if data[n][tree_index] >= tree_input:
            visible = False
            break
        else:
            visible = True
    return visible

def checktop(tree_input,index_input,tree_index):
    visible = False
    for n in range(0,index_input):
        if data[n][tree_index]>=tree_input:
            visible = False
            break
        else:
            visible = True
    return visible

def checkright(tree_input,row_input_r,index_input):
    visible_right = False
    for n in range(index_input+1, len(row_input_r)):
        if row_input_r[n]>=tree_input:
            visible_right=False
            break
        else:
            visible_right=True
            pass
    return visible_right

def checkleft(tree_input,row_input_l,index_input):
    visible_left = False
    for n in range(0,index_input):
        if row_input_l[n]>=tree_input:
            visible_left=False
            break
        else:
            visible_left=True
            pass
    return visible_left

def sum_checks(checks):
    sum = 0
    for check in checks:
        if check:
            sum += 1
            break
    return sum

def main(data):
    sum = 0
    for index, row in enumerate(data):
        if index == 0 or index == len(data)-1:
            sum += len(row)
        else:
            for index_tree,tree in enumerate(row):
                if index_tree == 0 or index_tree == len(row)-1:
                    sum+=1
                else:
                    checks = [checkright(tree,row,index_tree),checkleft(tree,row,index_tree),checktop(tree,index,index_tree),checkbottom(tree,index,index_tree)]
                    sum += sum_checks(checks)
    return sum

data = format_row_column()
sum = main(data)
print(sum)
