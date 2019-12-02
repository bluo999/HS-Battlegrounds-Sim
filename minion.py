import random

from effects import Effect, Effects
from minion_list import MINIONS
from tribe import Tribe


class Minion:

    def __init__(self, level, attack, health, mana,
                 tribe=Tribe.none, effects=[]):
        self.level = level
        self.attack = attack
        self.health = health
        self.tribe = tribe
        self.mana = mana
        self.effects = effects
        self.golden = False
        self.attacked = False

    def double_stats(self):
        self.attack *= 2
        self.health *= 2
        self.golden = True

    def has_effect(self, target_effect):
        for e in self.effects:
            if e.effect == target_effect:
                return e
        return None

    def is_tribe(self, tribe, count_none=False):
        return count_none or self.tribe == tribe or self.tribe == Tribe.amalgam

    def take_damage(self, damage, poisonous=False):
        effect = self.has_effect(Effects.divine_shield)
        if effect is not None:
            self.effects.remove(effect)
        elif poisonous:
            self.health = 0
        else:
            self.health -= damage

    def __str__(self):
        string = '('
        if self.has_effect(Effects.taunt) is not None:
            string += 'T '
        if self.has_effect(Effects.divine_shield) is not None:
            string += 'D '
        if self.has_effect(Effects.poisonous) is not None:
            string += 'P '
        string += f'{self.attack}/{self.health})'
        return string

    @staticmethod
    def new_minion(minion, golden=False):
        stats = MINIONS[minion]
        effects = []
        for effect in stats['effects']:
            valid = effect[0] != Effects.deathrattle_summon
            if valid and golden:
                if effect[0] == Effects.on_summon_tribe:
                    value = (effect[1][0], 2 * effect[1][1], 2 * effect[1][2])
                else:
                    value = 2 * effect[1]
            else:
                value = effect[1]
            effects.append(Effect(effect[0], value))
        m = Minion(stats['level'], stats['attack'], stats['health'],
                   stats['mana'], stats['tribe'], effects)
        if golden:
            m.double_stats()
        return m

    @staticmethod
    def random_minion(mana_cost):
        minion_pool = []
        for minion in MINIONS.keys():
            if MINIONS[minion]['mana'] == mana_cost:
                minion_pool.append(minion)
        choice = random.choice(minion_pool)
        return choice
