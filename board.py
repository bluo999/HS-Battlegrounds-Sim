import random
from effects import Effect, Effects
from minion import Minion
from tribe import Tribe


class Board:
    def __init__(self):
        self.minions = []

    def add_minion(self, minion):
        self.minions.append(minion)

    def board_attack(self, other, debug=False):
        attacker_index, attacker = self.choose_attacker()
        target_index, target = self.choose_target(other)

        if debug:
            print(f'({attacker_index}){attacker} attacks ' +
                  f'({target_index}){target}')

        attacker.take_damage(
            Board.total_attack(other, self, target, target_index),
            target.has_effect(Effects.poisonous) is not None
        )
        # Cleave
        cleave_effect = attacker.has_effect(Effects.cleave)
        attack = Board.total_attack(self, other, attacker, attacker_index)
        poisonous = attacker.has_effect(Effects.poisonous) is not None

        pre_minion = None
        post_minion = None

        if cleave_effect is not None:
            if target_index != 0:
                pre_minion = other.minions[target_index - 1]
                pre_minion.take_damage(attack, poisonous)
            if target_index != len(other.minions) - 1:
                post_minion = other.minions[target_index + 1]
                post_minion.take_damage(attack, poisonous)

        target.take_damage(attack, poisonous)
        attacker.attacked = True

        if attacker.health <= 0:
            self.kill_minion(other, attacker, attacker_index)
        if pre_minion is not None and pre_minion.health <= 0:
            other.kill_minion(other, pre_minion, target_index - 1)
            target_index -= 1
        if target.health <= 0:
            other.kill_minion(other, target, target_index)
            target_index -= 1
        if post_minion is not None and post_minion.health <= 0:
            other.kill_minion(other, post_minion, target_index + 1)

    def choose_attacker(self):
        attacker_index = -1
        for i, minion in enumerate(self.minions):
            if not minion.attacked:
                attacker_index = i
                break
        if attacker_index == -1:
            attacker_index = 0
            for i in range(len(self.minions)):
                self.minions[i].attacked = True

        attacker = self.minions[attacker_index]

        return attacker_index, attacker

    def choose_target(self, other):
        div = []
        for i, minion in enumerate(other.minions):
            if minion.has_effect(Effects.taunt) is not None:
                div.append(i)
        if len(div) == 0:
            target_index = random.randint(0, len(other.minions) - 1)
        else:
            target_index = random.choice(div)
        target = other.minions[target_index]

        return target_index, target

    def summon_minion(self, minion, minion_index, golden=False):
        # Deathrattle means 7, non means 6
        if len(self.minions) <= 7:
            new_minion = Minion.new_minion(minion, golden)
            current_attacker_index, _ = self.choose_attacker()
            new_minion.attacked = minion_index <= current_attacker_index
            self.minions.insert(minion_index + 1, new_minion)
            # Search for on summon tribe
            for i, m in enumerate(self.minions):
                if i != minion_index:
                    m_effect = m.has_effect(Effects.on_summon_tribe)
                    if m_effect is not None:
                        if (m_effect.value[0] == new_minion.tribe or
                                m_effect.value[0] == Tribe.amalgam):
                            m.attack += m_effect.value[1]
                            m.health += m_effect.value[2]
            # Search for give summon tribe
            for i, m in enumerate(self.minions):
                if i != minion_index:
                    m_effect = m.has_effect(Effects.give_summon_tribe)
                    if m_effect is not None:
                        buff = m_effect.value
                        if new_minion.is_tribe(buff[0]):
                            new_minion.attack += buff[1]
                            new_minion.health += buff[2]

    def kill_minion(self, other, minion, minion_index):
        # On deathrattle summon
        ds_effect = minion.has_effect(Effects.deathrattle_summon)
        if ds_effect is not None:
            if minion.has_effect(Effects.rat_pack) is not None:
                counter = 0
                while len(self.minions) <= 7 and counter <= minion.attack:
                    self.summon_minion(ds_effect.value, minion_index,
                                       minion.golden)
                    counter += 1
            else:
                self.summon_minion(ds_effect.value, minion_index,
                                   minion.golden)
        # On deathrattle random summon
        drs_effect = minion.has_effect(Effects.deathrattle_random)
        if drs_effect is not None:
            self.summon_minion(
                Minion.random_minion(drs_effect.value), minion_index
            )
        # On deathrattle effect
        d_effect = minion.has_effect(Effects.deathrattle_effect)
        if d_effect is not None:
            indices = list(range(len(self.minions)))
            indices.remove(minion_index)
            if len(indices) != 0:
                target_index = random.choice(indices)
                target_minion = self.minions[target_index]
                m_effect = target_minion.has_effect(d_effect.value[0])
                if m_effect is None:
                    target_minion.effects.append(
                        Effect(d_effect.value[0], d_effect.value[1])
                    )
        # On deathrattle damage
        dd_effect = minion.has_effect(Effects.deathrattle_damage)
        if dd_effect is not None:
            indices = list(range(len(other.minions)))
            for i in indices:
                if other.minions[i].health <= 0:
                    indices.remove(i)
            if len(indices) != 0:
                target_index = random.choice(indices)
                target_minion = other.minions[target_index]
                target_minion.take_damage(dd_effect.value)
                if target_minion.health <= 0:
                    other.kill_minion(self, target_minion, target_index)
        # On deathrattle tribe buff
        dtb_effect = minion.has_effect(Effects.deathrattle_tribe_buff)
        if dtb_effect is not None:
            print('dtb', minion, dtb_effect.value)
            indices = list(range(len(self.minions)))
            buff = dtb_effect.value
            for i in indices:
                target_minion = self.minions[i]
                if (target_minion.health > 0 and
                        target_minion.is_tribe(buff[0], count_none=True)):
                    target_minion.attack += buff[1]
                    target_minion.health += buff[2]
        # On death tribe
        for i, m in enumerate(self.minions):
            m_effect = m.has_effect(Effects.on_death_tribe)
            if m_effect is not None:
                buff = m_effect.value
                if minion.is_tribe(buff[0]):
                    m.attack += buff[1]
                    m.health += buff[2]

        del self.minions[minion_index]

    def __str__(self):
        string = ''
        for minion in self.minions:
            string += str(minion) + ','

        return string[:-1]

    @staticmethod
    def total_attack(board, other, minion, index):
        attack = 0
        # Adjacent attack buff
        if index != 0:
            effect = board.minions[index - 1].has_effect(Effects.adj_atk)
            if effect is not None:
                attack += effect.value
        if index != len(board.minions) - 1:
            effect = board.minions[index + 1].has_effect(Effects.adj_atk)
            if effect is not None:
                attack += effect.value

        # Tribe attack buff
        for i, m in enumerate(board.minions):
            if i != index:
                effect = m.has_effect(Effects.tribe_atk)
                if effect is not None and minion.is_tribe(effect.value[0]):
                    attack += effect.value[1]

        # Global tribe attack buff
        effect = minion.has_effect(Effects.global_tribe_atk)
        if effect is not None:
            for i, m in enumerate(board.minions):
                if i != index:
                    if minion.is_tribe(effect.value[0]):
                        attack += effect.value[1]
            for i, m in enumerate(other.minions):
                if minion.is_tribe(effect.value[0]):
                    attack += effect.value[1]

        return minion.attack + attack
