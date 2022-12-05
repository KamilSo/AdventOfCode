strat = open('Strat.txt', 'rt')
My_score = 0
X_score = 1
Y_score = 2
Z_score = 3
Win = 6
Draw = 3

def ScoreAdd(Me,Elf):
    if Me == 'X':
        Score = 0
        if Elf == 'A':
            Score = Score + Z_score
        elif Elf == 'C':
            Score = Score + Y_score
        elif Elf == 'B':
            Score = Score + X_score
    elif Me == 'Y':
        Score = Draw
        if Elf == 'A':
            Score = Score + X_score
        elif Elf == 'B':
            Score = Score + Y_score
        elif Elf == 'C':
            Score = Score + Z_score
    elif Me == 'Z':
        Score = Win
        if Elf == 'A':
            Score = Score + Y_score
        elif Elf == 'B':
            Score = Score + Z_score
        elif Elf == 'C':
            Score = Score + X_score
    return Score


for strats in strat:
    Elf = strats[0]
    Me = strats[2]
    My_score = My_score + ScoreAdd(Me,Elf)

print(My_score)

