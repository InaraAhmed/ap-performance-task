science_3 = ""
science_2 = ""
science_1 = ""
sciencerand = 0
music_3 = ""
music_2 = ""
music_1 = ""
musicrand = 0
sports_3 = ""
sports_2 = ""
sports_1 = ""
sportsrand = 0
sports1 = "soccer"
sports2 = "tennis"
sports3 = "court"
music1 = "track"
music2 = "album"
music3 = "artist"
science1 = "atoms"
science2 = "veins"
science3 = "proton"
math1 = "divide"
math2 = "factor"
math3 = "angle"
animal1 = "horse"
animal2 = "turtle"
animal3 = "parrot"
category = game.ask_for_string("Choose a category: sports, music or science", 7)
if category == "sports":
    sportsrand = randint(1, 3)
    if sportsrand == 1:
        sports_1 = game.ask_for_string("guess a six letter word", 6)
        if sports_1 == sports1:
            game.splash("Nice Job!")
        else:
            game.splash("Nope, better luck next time!")
    elif sportsrand == 2:
        sports_2 = game.ask_for_string("guess a six letter word", 6)
        if sports_2 == sports2:
            game.splash("Nice Job!")
        else:
            game.splash("Nope, better luck next time!")
    elif sportsrand == 3:
        sports_3 = game.ask_for_string("guess a six letter word", 6)
        if sports_3 == sports3:
            game.splash("Nice Job!")
        else:
            game.splash("Nope, better luck next time!")
elif category == "music":
    musicrand = randint(1, 3)
    if musicrand == 1:
        music_1 = game.ask_for_string("guess a five letter word", 5)
        if music_1 == music1:
            game.splash("Nice Job!")
        else:
            game.splash("Nope, better luck next time!")
    elif musicrand == 2:
        music_2 = game.ask_for_string("guess a five letter word", 5)
        if music_2 == music2:
            game.splash("Nice Job!")
        else:
            game.splash("Nope, better luck next time!")
    elif musicrand == 3:
        music_3 = game.ask_for_string("guess a six letter word", 6)
        if music_3 == music3:
            game.splash("Nice Job!")
        else:
            game.splash("Nope, better luck next time!")
elif category == "science":
    sciencerand = randint(1, 3)
    if sciencerand == 1:
        science_1 = game.ask_for_string("guess a five letter word", 5)
        if science_1 == science1:
            game.splash("Nice Job!")
        else:
            game.splash("Nope, better luck next time!")
    elif sciencerand == 2:
        science_2 = game.ask_for_string("guess a five letter word", 5)
        if science_2 == science2:
            game.splash("Nice Job!")
        else:
            game.splash("Nope, better luck next time!")
    elif sciencerand == 3:
        science_3 = game.ask_for_string("guess a six letter word", 6)
        if science_3 == science3:
            game.splash("Nice Job!")
        else:
            game.splash("Nope, better luck next time!")