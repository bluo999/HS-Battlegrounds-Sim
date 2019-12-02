m = Minion.new_minion(MinionList.cave_hydra)
m.attack = 24
m.health = 26
Board1.add_minion(m)
m = Minion.new_minion(MinionList.lightfang_enforcer)
m.attack = 2
m.health = 2
Board1.add_minion(m)
m = Minion.new_minion(MinionList.maexnna)
m.attack = 2
m.health = 8
Board1.add_minion(m)
m = Minion(2, 38, 38, Tribe.murloc,
           [Effect(Effects.tribe_atk, (Tribe.murloc, 2)),
            Effect(Effects.poisonous, 0), Effect(Effects.divine_shield, 0)])
Board1.add_minion(m)
m = Minion.new_minion(MinionList.nightmare_amalgam)
m.attack = 45
m.health = 46
m.effects.append(Effect(Effects.poisonous, 0))
m.effects.append(Effect(Effects.divine_shield, 0))
m.effects.append(Effect(Effects.taunt, 0))
Board1.add_minion(m)
m = Minion.new_minion(MinionList.siegebreaker)
m.attack = 37
m.health = 40
Board1.add_minion(m)
m = Minion.new_minion(MinionList.psych_o_tron)
m.attack = 39
m.health = 40
Board1.add_minion(m)

minions = []
m = Minion.new_minion(MinionList.cave_hydra)
m.attack = 12
m.health = 14
minions.append(m)
m = Minion(5, 27, 27, Tribe.beast,
           [Effect(Effects.deathrattle_tribe_buff, (Tribe.beast, 8, 8)),
            Effect(Effects.taunt, 0)])
minions.append(m)
m = Minion.new_minion(MinionList.nightmare_amalgam)
m.attack = 30
m.health = 31
m.effects.append(Effect(Effects.poisonous, 0))
m.effects.append(Effect(Effects.divine_shield, 0))
m.effects.append(Effect(Effects.taunt, 0))
minions.append(m)
m = Minion.new_minion(MinionList.rat_pack)
m.attack = 8
m.health = 8
minions.append(m)
m = Minion.new_minion(MinionList.maexnna)
m.attack = 12
m.health = 18
minions.append(m)
m = Minion(6, 17, 17, Tribe.beast,
           [Effect(Effects.give_summon_tribe, (Tribe.beast, 8, 8))])
minions.append(m)
m = Minion(2, 19, 19, Tribe.beast,
           [Effect(Effects.on_death_tribe, (Tribe.beast, 4, 2))])
minions.append(m)