# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define protoChar = Character("character1")
define vix = Character("Vixxy")

# The game starts here.



label splashscreen:
    scene bg room

    image splash = "images/logo-smaller.png"
    image splash-bg = "images/splash-bg.jpg"

    image splash:
        "images/logo-smaller.png"
        yalign 0.5

    scene black 
    with Pause(1)
    
    play sound "mus/intro-bloop.wav"

    scene splash-bg with dissolve

    show splash with dissolve
    with Pause(5)
    
    scene black with dissolve
    with Pause(1)

    return 

label start:
    image protoChar happy = "images/proto/character1-happy.png"
    image protoChar sad = "images/proto/character1-sad.png"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show protoChar happy

    # These display lines of dialogue.

    protoChar "WOAH"

    protoChar "HOLY SHIT"
    protoChar "I'M VERY VERY HAPPY"
    protoChar "HAHA"
    protoChar ":)"
    protoChar "SO FUNNY"

    show protoChar sad

    protoChar "OH FUCK"
    protoChar "OH FUCK"
    protoChar "OH SHIT"
    protoChar "I'M SAD NOW"
    protoChar "DAMNIT I AM CRYING NOW"
    protoChar ":("


    return
