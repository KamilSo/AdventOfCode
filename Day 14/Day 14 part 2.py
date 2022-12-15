import copy
import numpy

rocks = open('input.txt', 'rt')
rocks = [x.replace('\n', '').split(' -> ') for x in rocks]
parsed_rocks = []
rock_coords = []
for rock in rocks:
    rocks = [x.split(',') for x in rock]
    parsed_rocks.append(rocks)

for data in parsed_rocks:
    for index, coord in enumerate(data):
        if index == len(data) - 1:
            break
        else:
            y_diff = int(data[index + 1][1]) - int(coord[1])
            x_diff = int(data[index + 1][0]) - int(coord[0])
            coord_temp = copy.deepcopy(coord)
            rock_coords.append(coord_temp)
            if x_diff == 0:
                for i in range(abs(y_diff)):
                    coord[1] = int(coord[1])
                    coord[1] += numpy.sign(y_diff)
                    coord_temp = copy.deepcopy(coord)
                    rock_coords.append(coord_temp)
            elif y_diff == 0:
                for i in range(abs(x_diff)):
                    coord[0] = int(coord[0])
                    coord[0] += numpy.sign(x_diff)
                    coord_temp = copy.deepcopy(coord)
                    rock_coords.append(coord_temp)

sorted_rock_coords = []
max_y = 0
for rock in rock_coords:
    if max_y < int(rock[1]):
        max_y = int(rock[1])
    for index, coord in enumerate(rock):
        rock[index] = int(coord)
    if rock not in sorted_rock_coords:
        sorted_rock_coords.append(rock)

max_y += 2
print(sorted_rock_coords)
print(max_y)

sand = []
end = False
n=1
while not end:
    stop = False
    sand_coord = [500, 0]
    while not stop:
        if sand_coord not in sorted_rock_coords and sand_coord not in sand:
            sand_coord[1] += 1
            if sand_coord[1] == max_y:
                sand_coord[1] -= 1
                if sand_coord not in sand and sand_coord not in sorted_rock_coords:
                    sand.append(sand_coord)
                stop = True
                break
            if sand_coord in sorted_rock_coords or sand_coord in sand:
                sand_coord[0] -= 1
                if sand_coord in sorted_rock_coords or sand_coord in sand:
                    sand_coord[0] += 2
                    if sand_coord in sorted_rock_coords or sand_coord in sand:
                        sand_coord[0] -= 1
                        sand_coord[1] -= 1
                        sand.append(sand_coord)
                        stop = True
    if sand[-1] == [500,0]:
        end = True
        break
    print(len(sand))

print(len(sand)+(n-1)*500)