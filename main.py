def on_button_pressed_a():
    global p1, p2
    p1 = randint(0, 4)
    p2 = randint(0, 4)
    basic.show_string("" + (villains[p1]))
    basic.show_string("VS")
    basic.show_string("" + (heroes[p2]))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global hero_score, villain_score
    if p1 > p2:
        basic.show_string("" + str((heroes)))
        basic.show_string("wins!")
        hero_score += 1
        basic.show_string("heroes")
        basic.show_number(hero_score)
    else:
        basic.show_string("" + str((villains)))
        basic.show_string("wins!")
        villain_score += 1
        basic.show_string("villains")
        basic.show_number(villain_score)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

villain_score = 0
hero_score = 0
p2 = 0
p1 = 0
villains: List[str] = []
heroes: List[str] = []
heroes = ["batman",
    "spiderman",
    "wolverine",
    "captain america",
    "ALFRED"]
villains = ["Thanos", "dr.doom", "joker", "venom", "joker who laughs "]

def on_forever():
    global villain_score, hero_score
    villain_score = 0
    hero_score = 0
basic.forever(on_forever)
