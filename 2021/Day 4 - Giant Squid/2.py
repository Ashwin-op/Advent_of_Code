import re


def playBoards():
    global gameboards
    for i in numbers:
        gameboards = [
            [re.sub(f"^{str(i)}$", "x", k) for k in x] for x in gameboards
        ]
        for idx, gameboard in enumerate(gameboards):
            if any(["".join(gameboard[i*5:i*5+5]) == "xxxxx" for i in range(5)]) or any(["".join(gameboard[i::5]) == "xxxxx" for i in range(5)]):
                yield sum([int(i) for i in gameboard if type(i) == int or i.isdigit()]) * i
                del gameboards[idx]


with open("input.txt") as file:
    temp = file.read().split('\n\n')
    numbers = list(map(int, temp[0].split(',')))
    gameboards = [
        re.sub("\s+", " ", x.replace("\n", " ")).split()
        for x in temp[1:]
    ]
    print(list(playBoards())[-1])
