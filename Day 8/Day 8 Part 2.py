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
    if index_input == len(data)-1:
        return 1
        pass
    else:
        sum = 0
        for n in range(index_input+1,len(data)):
            if data[n][tree_index] >= tree_input:
                sum +=1
                break
            else:
                sum +=1
        return sum

def checktop(tree_input,index_input,tree_index):
    if index_input == 0:
        return 1
        pass
    else:
        sum = 0
        for n in range(index_input-1,-1,-1):
            if data[n][tree_index]>=tree_input:
                sum+=1
                break
            else:
                sum+=1
        return sum

def checkright(tree_input,row_input,index_input):
    if index_input == len(row_input):
        return 1
        pass
    else:
        sum = 0
        for n in range(index_input+1, len(row_input)):
            if row_input[n]>=tree_input:
                sum+=1
                break
            else:
                sum+=1
                pass
        return sum

def checkleft(tree_input,row_input,index_input):
    if index_input == 0:
        return 1
        pass
    else:
        sum = 0
        for n in range(index_input-1,-1,-1):
            if row_input[n]>=tree_input:
                sum+=1
                break
            else:
                sum+=1
                pass
        return sum

def multiply_checks(checks):
    product = 1
    for element in checks:
        product = element*product
    return product

def main(data):
    max_sum = 0
    for index, row in enumerate(data):
        for index_tree,tree in enumerate(row):
            checks = [checkright(tree,row,index_tree),checkleft(tree,row,index_tree),
                      checktop(tree,index,index_tree),checkbottom(tree,index,index_tree)]
            sum = multiply_checks(checks)
            if sum > max_sum:
                max_sum = sum
    return max_sum

data = format_row_column()
sum = main(data)
print(sum)
