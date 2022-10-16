def compute_game_state(name_p1, name_p2, wins):
    points = [0, 15, 30, 40]
    nbr_win_p1 = wins.count(name_p1)
    nbr_win_p2 = wins.count(name_p2)
    if nbr_win_p1 < 3 and nbr_win_p2 < 3:
        if nbr_win_p1 != nbr_win_p2:
            return f'{name_p1} {points[nbr_win_p1]} - {name_p2} {points[nbr_win_p2]}'
        else:
            return f'{points[nbr_win_p1]}a'
    else:
        if nbr_win_p1 == nbr_win_p2:
            return 'DEUCE'
        else:
            if abs(nbr_win_p1 - nbr_win_p2) == 1:
                return f'{name_p1} ADVANTAGE' if nbr_win_p1 > nbr_win_p2 else f'{name_p2} ADVANTAGE'
            else:
                return f'{name_p1} WINS' if nbr_win_p1 > nbr_win_p2 else f'{name_p2} WINS'

def main():
    # pylint: disable = C, W
    name_p1 = input()
    name_p2 = input()
    played_count = int(input())
    wins = []
    for i in range(played_count):
        wins.append(input())
    print(compute_game_state(name_p1, name_p2, wins))


if __name__ == "__main__":
    main()
