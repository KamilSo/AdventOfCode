Vars = open('Elf.txt', 'rt')
Elf_max = 0
sum = 0
lines = Vars.readlines()
for line in lines:
    if line == '\n':
         if sum>Elf_max:
             Elf_max = sum
         sum = 0
    else:
         sum = sum  + int(line)
print(Elf_max)
