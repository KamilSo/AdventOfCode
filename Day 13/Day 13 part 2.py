packets = [x for x in open('input.txt', 'rt') if x != '']
packets = [x.replace('\n', '') for x in packets if x != '\n']


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


for n in range(len(packets)):
    for index, packet in enumerate(packets):
        if index == len(packets) - 1:
            break
        if Main(eval(packet), eval(packets[index + 1])) < 0:
            continue
        else:
            packets[index], packets[index + 1] = packets[index + 1], packet
            continue

decoder_key = 1
for index, sorted_packet in enumerate(packets):
    if eval(sorted_packet) == [[2]]:
        decoder_key *= index + 1
    elif eval(sorted_packet) == [[6]]:
        decoder_key *= index + 1
        break
print(decoder_key)
