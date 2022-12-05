Vars = open('Elf.txt', 'rt')
Elf_max = []
sum = 0
lines = Vars.readlines()
for line in lines:
    if line == '\n':
         Elf_max.append(sum)
         sum = 0
    else:
         sum = sum  + int(line)

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

bubble_sort(Elf_max)
sum = Elf_max[-1]+Elf_max[-2]+Elf_max[-3]
print(sum)


