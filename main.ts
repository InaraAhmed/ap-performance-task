let mathask = ""
let mathrand = ""
let scienceask = ""
let sciencerand = ""
let musicask = ""
let musicrand = ""
let sportsask = ""
let sportsrand = ""
let sportslist = ["soccer", "tennis", "court"]
let musiclist = ["track", "album", "artist"]
let sciencelist = ["atoms", "veins", "proton"]
let mathlist = ["divide", "factor", "angle"]
let play = game.askForString("Would you like to play Guess?", 3)
while (play == "yes") {
    game.splash("Choose a category")
    story.showPlayerChoices("sports", "music", "science", "math")
    if (story.checkLastAnswer("sports")) {
        sportsrand = sportslist._pickRandom()
        sportsask = game.askForString("guess a six letter word", 6)
        if (sportsask == sportsrand) {
            game.splash("Nice Job!")
        } else {
            game.splash("Nope, better luck next time!")
        }
    } else if (story.checkLastAnswer("music")) {
        musicrand = musiclist._pickRandom()
        musicask = game.askForString("guess a six letter word", 6)
        if (sportsrand == sportsask) {
            game.splash("Nice Job!")
        } else {
            game.splash("Nope, better luck next time!")
        }
    } else if (story.checkLastAnswer("science")) {
        sciencerand = sciencelist._pickRandom()
        scienceask = game.askForString("guess a six letter word", 6)
        if (sciencerand == scienceask) {
            game.splash("Nice Job!")
        } else {
            game.splash("Nope, better luck next time!")
        }
    } else if (story.checkLastAnswer("math")) {
        mathrand = mathlist._pickRandom()
        mathask = game.askForString("guess a six letter word", 6)
        if (mathrand == mathask) {
            game.splash("Nice Job!")
        } else {
            game.splash("Nope, better luck next time!")
        }
    }
    play = game.askForString("Would you like to play Guess?", 3)
}
