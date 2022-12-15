packets = open('input.txt', 'rt').read().strip().split('\n\n')
packets = [x.split('\n') for x in packets]
print(packets)


def Main(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return Main([x], y)
    else:
        if type(y) == int:
            return Main(x, [y])
    for value_1, value_2 in zip(x, y):
        comapare = Main(value_1, value_2)
        if comapare:
            return comapare
    return len(x) - len(y)

counter = 0
for index,(packet_1,packet_2) in enumerate(packets):
    if Main(eval(packet_1),eval(packet_2)) < 0:
        counter += index + 1

print(counter)
