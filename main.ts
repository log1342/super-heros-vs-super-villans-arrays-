input.onButtonPressed(Button.A, function () {
    p1 = randint(0, 4)
    p2 = randint(0, 4)
    basic.showString("" + (villains[p1]))
    basic.showString("VS")
    basic.showString("" + (heroes[p2]))
})
input.onButtonPressed(Button.AB, function () {
    if (p1 > p2) {
        basic.showString("" + (heroes))
        basic.showString("wins!")
        hero_score += 1
        basic.showString("heroes")
        basic.showNumber(hero_score)
    } else {
        basic.showString("" + (villains))
        basic.showString("wins!")
        villain_score += 1
        basic.showString("villains")
        basic.showNumber(villain_score)
    }
})
let p2 = 0
let p1 = 0
let villains: string[] = []
let heroes: string[] = []
let hero_score = 0
let villain_score = 0
villain_score = 0
hero_score = 0
heroes = [
"batman",
"spiderman",
"wolverine",
"captain america",
"deadpool"
]
villains = [
"Thanos",
"dr.doom",
"joker",
"venom",
"joker who laughs "
]
let hero_rating = [
7,
6,
8,
8.8,
9
]
let villain_rating = [
8.2,
8.9,
7,
5,
10
]
basic.forever(function () {
	
})
