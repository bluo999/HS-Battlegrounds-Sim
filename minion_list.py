import enum

from effects import Effects
from tribe import Tribe

# TODO: spawn of n'zoth, golden cards


class MinionList(enum.Enum):
    alleycat = 1
    tabbycat = 101
    dire_wolf_alpha = 2
    mecharoo = 3
    jo_e_bot = 103
    micro_machine = 4
    murloc_tidecaller = 5
    murloc_tidehunter = 6
    murloc_scout = 106
    righteous_protector = 7
    rockpool_hunter = 8
    selfless_hero = 9
    voidwalker = 10
    vulgar_homunculus = 11
    wrath_weaver = 12

    annoy_o_tron = 20
    coldlight_seer = 21
    harvest_golem = 22
    damaged_golem = 122
    kaboom_bot = 23
    kindly_grandmother = 24
    big_bad_wolf = 124
    metaltooth_leaper = 25
    mounted_rapter = 26
    murloc_warleader = 27
    nathrezim_overseer = 28
    nightmare_amalgam = 29
    old_murk_eye = 30
    pogo_hopper = 31
    rat_pack = 32
    rat = 33
    scavenging_hyena = 34
    shielded_minibot = 35
    spawn_of_nzoth = 36
    zoobot = 37

    cave_hydra = 200
    goldrinn_the_great_wolf = 201
    maexnna = 202
    mama_bear = 203
    lightfang_enforcer = 204
    siegebreaker = 205
    psych_o_tron = 206


MINIONS = {
    MinionList.alleycat: {
        "level": 1,
        "attack": 1,
        "health": 1,
        "mana": 1,
        "tribe": Tribe.beast,
        "effects": [],
    },
    MinionList.tabbycat: {
        "level": 1,
        "attack": 1,
        "health": 1,
        "mana": 0,
        "tribe": Tribe.beast,
        "effects": [],
    },
    MinionList.dire_wolf_alpha: {
        "level": 1,
        "attack": 2,
        "health": 2,
        "mana": 2,
        "tribe": Tribe.beast,
        "effects": [(Effects.adj_atk, 1)]
    },
    MinionList.mecharoo: {
        "level": 1,
        "attack": 1,
        "health": 1,
        "mana": 1,
        "tribe": Tribe.mech,
        "effects": [(Effects.deathrattle_summon, MinionList.jo_e_bot)],
    },
    MinionList.jo_e_bot: {
        "level": 1,
        "attack": 1,
        "health": 1,
        "mana": 0,
        "tribe": Tribe.mech,
        "effects": [],
    },
    MinionList.micro_machine: {
        "level": 1,
        "attack": 1,
        "health": 2,
        "mana": 2,
        "tribe": Tribe.mech,
        "effects": [],
    },
    MinionList.murloc_tidecaller: {
        "level": 1,
        "attack": 1,
        "health": 2,
        "mana": 1,
        "tribe": Tribe.murloc,
        "effects": [(Effects.on_summon_tribe, (Tribe.murloc, 1, 0))],
    },
    MinionList.murloc_tidehunter: {
        "level": 1,
        "attack": 2,
        "health": 1,
        "mana": 2,
        "tribe": Tribe.murloc,
        "effects": [],
    },
    MinionList.murloc_scout: {
        "level": 1,
        "attack": 1,
        "health": 1,
        "mana": 0,
        "tribe": Tribe.murloc,
        "effects": [],
    },
    MinionList.righteous_protector: {
        "level": 1,
        "attack": 1,
        "health": 1,
        "mana": 1,
        "tribe": Tribe.none,
        "effects": [(Effects.divine_shield, 0), (Effects.taunt, 0)],
    },
    MinionList.rockpool_hunter: {
        "level": 1,
        "attack": 2,
        "health": 3,
        "mana": 2,
        "tribe": Tribe.murloc,
        "effects": [],
    },
    MinionList.selfless_hero: {
        "level": 1,
        "attack": 2,
        "health": 1,
        "mana": 1,
        "tribe": Tribe.none,
        "effects": [(Effects.deathrattle_effect, (Effects.divine_shield, 0))],
    },
    MinionList.voidwalker: {
        "level": 1,
        "attack": 1,
        "health": 3,
        "mana": 1,
        "tribe": Tribe.demon,
        "effects": [(Effects.taunt, 0)],
    },
    MinionList.vulgar_homunculus: {
        "level": 1,
        "attack": 2,
        "health": 4,
        "mana": 2,
        "tribe": Tribe.demon,
        "effects": [(Effects.taunt, 0)],
    },
    MinionList.wrath_weaver: {
        "level": 1,
        "attack": 1,
        "health": 1,
        "mana": 1,
        "tribe": Tribe.demon,
        "effects": [],
    },

    MinionList.annoy_o_tron: {
        "level": 2,
        "attack": 1,
        "health": 2,
        "mana": 2,
        "tribe": Tribe.mech,
        "effects": [(Effects.taunt, 0), (Effects.divine_shield, 0)],
    },
    MinionList.coldlight_seer: {
        "level": 2,
        "attack": 2,
        "health": 3,
        "mana": 3,
        "tribe": Tribe.murloc,
        "effects": [],
    },
    MinionList.harvest_golem: {
        "level": 2,
        "attack": 2,
        "health": 3,
        "mana": 3,
        "tribe": Tribe.mech,
        "effects": [(Effects.deathrattle_summon, MinionList.damaged_golem)],
    },
    MinionList.damaged_golem: {
        "level": 2,
        "attack": 2,
        "health": 1,
        "mana": 0,
        "tribe": Tribe.mech,
        "effects": [],
    },
    MinionList.kaboom_bot: {
        "level": 2,
        "attack": 2,
        "health": 2,
        "mana": 3,
        "tribe": Tribe.mech,
        "effects": [(Effects.deathrattle_damage, 4)],
    },
    MinionList.kindly_grandmother: {
        "level": 2,
        "attack": 1,
        "health": 1,
        "mana": 2,
        "tribe": Tribe.beast,
        "effects": [(Effects.deathrattle_summon, MinionList.big_bad_wolf)],
    },
    MinionList.big_bad_wolf: {
        "level": 1,
        "attack": 3,
        "health": 2,
        "mana": 0,
        "tribe": Tribe.beast,
        "effects": [],
    },
    MinionList.metaltooth_leaper: {
        "level": 2,
        "attack": 3,
        "health": 3,
        "mana": 3,
        "tribe": Tribe.mech,
        "effects": [],
    },
    MinionList.mounted_rapter: {
        "level": 2,
        "attack": 3,
        "health": 2,
        "mana": 3,
        "tribe": Tribe.beast,
        "effects": [(Effects.deathrattle_random, 1)],
    },
    MinionList.murloc_warleader: {
        "level": 2,
        "attack": 3,
        "health": 3,
        "mana": 3,
        "tribe": Tribe.murloc,
        "effects": [(Effects.tribe_atk, (Tribe.murloc, 2))],
    },
    MinionList.nathrezim_overseer: {
        "level": 2,
        "attack": 2,
        "health": 4,
        "mana": 3,
        "tribe": Tribe.demon,
        "effects": [],
    },
    MinionList.nightmare_amalgam: {
        "level": 2,
        "attack": 3,
        "health": 4,
        "mana": 3,
        "tribe": Tribe.amalgam,
        "effects": [],
    },
    MinionList.old_murk_eye: {
        "level": 2,
        "attack": 2,
        "health": 4,
        "mana": 4,
        "tribe": Tribe.murloc,
        "effects": [(Effects.global_tribe_atk, (Tribe.murloc, 1))],
    },
    MinionList.pogo_hopper: {
        "level": 2,
        "attack": 1,
        "health": 1,
        "mana": 2,
        "tribe": Tribe.mech,
        "effects": [],
    },
    MinionList.rat_pack: {
        "level": 2,
        "attack": 2,
        "health": 2,
        "mana": 3,
        "tribe": Tribe.beast,
        "effects": [(Effects.deathrattle_summon, MinionList.rat),
                    (Effects.rat_pack, 0)],
    },
    MinionList.rat: {
        "level": 1,
        "attack": 1,
        "health": 1,
        "mana": 0,
        "tribe": Tribe.beast,
        "effects": [],
    },
    MinionList.scavenging_hyena: {
        "level": 2,
        "attack": 2,
        "health": 2,
        "mana": 2,
        "tribe": Tribe.beast,
        "effects": [(Effects.on_death_tribe, (Tribe.beast, 2, 1))],
    },
    MinionList.shielded_minibot: {
        "level": 2,
        "attack": 2,
        "health": 2,
        "mana": 2,
        "tribe": Tribe.mech,
        "effects": [(Effects.divine_shield, 0)],
    },
    MinionList.spawn_of_nzoth: {
        "mana": 3,
    },
    MinionList.zoobot: {
        "level": 2,
        "attack": 3,
        "health": 3,
        "mana": 3,
        "tribe": Tribe.mech,
        "effects": [],
    },

    MinionList.cave_hydra: {
        "level": 4,
        "attack": 2,
        "health": 4,
        "mana": 3,
        "tribe": Tribe.beast,
        "effects": [(Effects.cleave, 0)],
    },
    MinionList.goldrinn_the_great_wolf: {
        "level": 5,
        "attack": 4,
        "health": 4,
        "mana": 8,
        "tribe": Tribe.none,
        "effects": [(Effects.deathrattle_tribe_buff, (Tribe.beast, 4, 4))],
    },
    MinionList.maexnna: {
        "level": 6,
        "attack": 2,
        "health": 8,
        "mana": 6,
        "tribe": Tribe.beast,
        "effects": [(Effects.poisonous, 0)],
    },
    MinionList.mama_bear: {
        "level": 6,
        "attack": 4,
        "health": 4,
        "mana": 8,
        "tribe": Tribe.beast,
        "effects": [(Effects.give_summon_tribe, (Tribe.beast, 4, 4))],
    },
    MinionList.lightfang_enforcer: {
        "level": 5,
        "attack": 2,
        "health": 2,
        "mana": 6,
        "tribe": Tribe.none,
        "effects": [],
    },
    MinionList.siegebreaker: {
        "level": 4,
        "attack": 5,
        "health": 8,
        "mana": 7,
        "tribe": Tribe.none,
        "effects": [(Effects.taunt, 0), (Effects.tribe_atk, (Tribe.demon, 1))],
    },
    MinionList.psych_o_tron: {
        "level": 3,
        "attack": 3,
        "health": 4,
        "mana": 5,
        "tribe": Tribe.mech,
        "effects": [(Effects.taunt, 0), (Effects.divine_shield, 0)],
    },
}
