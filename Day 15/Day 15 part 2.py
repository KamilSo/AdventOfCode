Data = [x.replace('Sensor at ', '').replace(' closest beacon is at ', '').replace(' ', '').replace(
    '\n', '').replace('=', '').replace('x', '').replace('y', '').replace(',', ' ') for x in open('input.txt', 'rt')]
Data = [x.split(':') for x in Data]
parsed_data = []
for x in Data:
    Data = [y.split(' ') for y in x]
    parsed_data.append(Data)

answer = [0, 0]  # [min,max]

for y_row in range(21):
    print(y_row)
    for coords in parsed_data:
        sensor_x = int(coords[0][0])
        sensor_y = int(coords[0][1])
        beacon_x = int(coords[1][0])
        beacon_y = int(coords[1][1])
        Sensor_y_diff = abs(y_row - abs(sensor_y))
        Manhattan_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        if Sensor_y_diff < Manhattan_distance:
            append_coord = sensor_x + Manhattan_distance - Sensor_y_diff
            append_coord_2 = sensor_x - (Manhattan_distance - Sensor_y_diff)
            if answer == [0,0]:
                if append_coord != beacon_x:
                    answer[1] = append_coord
                    if append_coord_2 != beacon_x:
                        answer[0] = append_coord_2
                if append_coord_2 != beacon_x:
                    answer[0] = append_coord_2
                    if append_coord != beacon_x:
                        answer[1] = append_coord
            else:
    if answer == [0,20]:
        answer = [0,0]
    else:
        print(answer)
        exit(0)


print(parsed_data)
