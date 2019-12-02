import random


def simulate(boards, debug=False):
    attacker = random.randint(0, 1)

    if debug:
        print(f'Start: Player {attacker+1}')
        print('-----')
        for i, board in enumerate(boards):
            print(f'{i+1}: {board}')

    while len(boards[0].minions) != 0 and len(boards[1].minions) != 0:
        boards[attacker].board_attack(boards[1 - attacker], debug=debug)
        attacker = 1 - attacker
        if debug:
            print(f'\nState: Player {attacker+1}')
            print('-----')
            for i, board in enumerate(boards):
                print(f'{i+1}: {board}')

    # print('End')
    # for i, board in enumerate(boards):
    #     print(f'{i+1}: {board}')

    dmg = 0
    if len(boards[0].minions) == 0:
        if len(boards[1].minions) == 0:
            if debug:
                print('\nTie')
            return (0, dmg)
        if debug:
            print('\nPlayer 2 Won')
        for minion in boards[1].minions:
            dmg += minion.level
        return (2, dmg)
    if debug:
        print('\nPlayer 1 Won')
    for minion in boards[0].minions:
        dmg += minion.level
    return (1, dmg)
