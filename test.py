import copy

from statistics import median

from battlegrounds import simulate
from board import Board
from effects import Effect, Effects
from minion import Minion
from minion_list import MinionList
from tribe import Tribe

Board1 = Board()
Board2 = Board()

Board1.add_minion(Minion.new_minion(MinionList.nightmare_amalgam))
Board1.add_minion(Minion.new_minion(MinionList.dire_wolf_alpha))
Board2.add_minion(Minion.new_minion(MinionList.kaboom_bot))

stats = {
    0: 0,
    1: 0,
    2: 0,
}
damage = {
    1: [],
    2: [],
}

total = 10000
for i in range(total):
    B1 = copy.deepcopy(Board1)
    B2 = copy.deepcopy(Board2)
    winner, dmg = simulate([B1, B2], debug=(i == 0))
    stats[winner] += 1
    if winner != 0:
        damage[winner].append(dmg)

tie = stats[0] / total * 100
p1_win = stats[1] / total * 100
p2_win = stats[2] / total * 100
p1_dmg = median(damage[1]) if len(damage[1]) > 0 else 0
p2_dmg = median(damage[2]) if len(damage[2]) > 0 else 0

print('\nOverall stats:')
print(f'Player 1 wins ~{p1_win:.2f}% ({stats[1]}) (median damage: {p1_dmg})')
print(f'Player 2 wins ~{p2_win:.2f}% ({stats[2]}) (median damage: {p2_dmg})')
print(f'Tie           ~{tie:.2f}% ({stats[0]}) of the time')
