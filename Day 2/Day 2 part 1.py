strat = open('Strat.txt', 'rt')
My_score = 0
X_score = 1
Y_score = 2
Z_score = 3
Win = 6
Draw = 3

def ScoreAdd(Me,Elf):
    if Me == 'X':
        Score = X_score
        if Elf == 'A':
            Score = Score + Draw
        elif Elf == 'C':
            Score = Score + Win
    elif Me == 'Y':
        Score = Y_score
        if Elf == 'A':
            Score = Score + Win
        elif Elf == 'B':
            Score = Score + Draw
    elif Me == 'Z':
        Score = Z_score
        if Elf == 'B':
            Score = Score + Win
        elif Elf == 'C':
            Score = Score + Draw
    return Score


for strats in strat:
    Elf = strats[0]
    Me = strats[2]
    My_score = My_score + ScoreAdd(Me,Elf)

print(My_score)

