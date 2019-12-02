import enum


class Effects(enum.Enum):
    none = 0

    taunt = 1
    divine_shield = 2
    poisonous = 3
    cleave = 4
    deathrattle_summon = 5  # value: MinionList
    deathrattle_effect = 6  # value: Effects
    deathrattle_damage = 7  # value: damage ammount
    deathrattle_tribe_buff = 8  # value: (Tribe, attack, health)
    deathrattle_random = 9  # value: mana cost

    on_summon_tribe = 10  # (tidehunter) value: (Tribe, attack, health)
    give_summon_tribe = 11  # (mama bear) value: (Tribe, attack, health)
    on_death_tribe = 12  # (scavengeing hyena) value: (Tribe, attack, health)

    adj_atk = 15
    tribe_atk = 16  # (murloc warleader) value: (Tribe, attack)
    global_tribe_atk = 17  # (old murk eye) value: (Tribe, attack)

    rat_pack = 99


class Effect:
    def __init__(self, effect, value=None):
        self.effect = effect
        self.value = value
