from asciimon_game.moves import MOVES, type_multi
from asciimon_game.art import ART
from asciimon_game.ui import hp_bar, pause, clear_screen, ask_choice
import random


def calc_damage(attacker, defender, move_name, roll=1.0):
    move = MOVES[move_name]
    power = move["power"]
    move_type = move["type"]
    multiplier = type_multi(move_type, defender.type)
    attack_total = power * (attacker.attack/defender.defense) * multiplier * roll
    attack_total = round(attack_total)
    attack_total = max(1, attack_total)
    return attack_total

def draw_battle(mine, enemy):
    enemy_info = [ 
        f"{enemy.name.upper()}  Lv{enemy.level}",
        "HP " + hp_bar(enemy.hp, enemy.max_hp) + f" {enemy.hp}/{enemy.max_hp}",
        "",
        "",
        "",
    ]
    
    enemy_art = ART[enemy.species]

    for info, art in zip(enemy_info, enemy_art):
        print(info.ljust(30) + art)

    print()

    mine_info = [
        f"{mine.name.upper()}  Lv{mine.level}",
        "HP " + hp_bar(mine.hp, mine.max_hp) + f" {mine.hp}/{mine.max_hp}",
        "",
        "",
        "",
    ]

    mine_art = ART[mine.species]

    for info,art in zip(mine_info, mine_art):
        print(art + "   " + info)

def battle(player, enemy_party, wild):
    mine = player.first_healthy()
    enemy = enemy_party[0]
    while True:
        clear_screen()
        draw_battle(mine, enemy)
        choice = ask_choice(f"What will {mine.name.upper()} do?", mine.moves)
        my_move = mine.moves[choice]
        enemy_move = random.choice(enemy.moves)
        if mine.speed > enemy.speed:
            player_first = True
        elif mine.speed < enemy.speed:
            player_first = False
        else:
            player_first = random.choice([True, False])
        if player_first:
            order = [(mine, enemy, my_move), (enemy, mine, enemy_move)]
        else:
            order = [(enemy, mine, enemy_move), (mine, enemy, my_move)]
        for attacker, defender, move in order:
            do_attack(attacker, defender, move)
            if defender.is_fainted():
                clear_screen()
                draw_battle(mine, enemy)
                print(f"{defender.name.upper()} fainted!")
                pause()
                if defender is enemy:
                    print(f"{player.name} won the battle!")
                    pause()
                    return "won"
                print(f"{player.name} blacked out...") 
                print("... and rushed back to town to heal!")
                pause()
                return "lost"

def do_attack(attacker, defender, move_name):
    print(f"{attacker.name.upper()} used {move_name}!")
    give_damage = calc_damage(attacker, defender, move_name, roll=random.uniform(0.85, 1.0))
    defender.take_damage(give_damage)
    effectiveness = type_multi(MOVES[move_name]["type"], defender.type)
    if effectiveness == 2.0:
        print("It's super effective!")
    elif effectiveness == 0.5:
        print("It's not very effective...")
    pause()

