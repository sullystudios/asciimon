def clear_screen():
    print("\033[2J\033[H", end="")

def pause():
    input("(press Enter)")

def hp_bar(hp, max_hp, width=10):
    hp_percentage = hp / max_hp
    how_many_hash = hp_percentage * width
    how_many_hash = round(how_many_hash)
    if hp > 0  and how_many_hash == 0:
        how_many_hash = 1
    if hp < max_hp and how_many_hash == width:
        how_many_hash = width - 1
    how_many_dash = width - how_many_hash
    hash_on_bar = "#" * how_many_hash
    dash_on_bar = "-" * how_many_dash
    vis_hp_bar = "[" + hash_on_bar + dash_on_bar + "]"
    return vis_hp_bar

def ask_choice(prompt, options):
    print(prompt)
    for number, option in enumerate(options, start=1):
        print(f"{number}) {option}")
    while True:
        answer = input("> ")
        try:
            number = int(answer)
        except ValueError:
            continue
        if number >= 1 and number <= len(options):
            return number - 1

def ask_text(prompt, allow_blank=False, max_len=12):
    while True:
        answer = input(prompt + " ")
        answer = answer.strip()
        if len(answer) > max_len:
            print(f"Max {max_len} characters")
            continue
        if answer == "" and not allow_blank:
            print("Please Enter a name")
            continue
        return answer