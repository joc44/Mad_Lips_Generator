def stroy1():
    verb = input("Enter a verb ending s: ")
    body = input("Enter a body part: ")
    body1 = input("Enter a body part: ")
    verb1 = input("Enter a verb ending s: ")
    body2 = input("Enter a body part: ")
    body3 = input("Enter a body part: ")
    verb2 = input("Enter a verb ending s: ")
    adj = input("Enter a adjective: ")
    adj1 = input("Enter a adjective: ")
    adj2 = input("Enter a adjective: ")
    body4 = input("Enter a body part: ")
    body5 = input("Enter a body part: ")
    body6 = input("Enter a body part: ")
    body7 = input("Enter a body part: ")
    verb3 = input("Enter a verb ending s: ")
    noun = input("Enter a noun: ")
    body8 = input("Enter a body part: ")
    noun1 = input("Enter a noun: ")
    body9 = input("Enter a body part: ")
    body10 = input("Enter a body part: ")
    body11 = input("Enter a body part: ")
    adverb = input("Enter a adverb: ")
    adj3 = input("Enter a adjective: ")
    noun2 = input("Enter a noun: ")
    adj4 = input("Enter a adjective: ")
    adj5 = input("Enter a adjective: ")
    verb4 = input("Enter a verb ending s: ")



    print( f"He {verb} his {body} so his {body1} pushes against me.. Yes.Right there...He {verb1} his {body2} along my {body3}, \n" \
           f"eases back,then {verb2} into me again-so {adj}, so {adj1}, so {adj2} - his {body4} pressing down on me, his {body5} and his \n" \
           f"{body6} on either side of my {body7}. 'Oh, Ana', he {verb3} as he lets go, my name a {noun} on his {body8} as he finds his {noun1}.\n" \
           f"His {body9} rests on my {body10}, his {body11} wrapped around me...I just want to enjoy the {adverb} {adj3} afterglow of making {noun2} \n" \
           f"with Christian Grey, because that's what we've done: {adj4},{adj5} {verb4}. ")

def story2():
    adj = input("Enter a adjective: ")
    adj1 = input("Enter a adjective: ")
    tib = input("Enter a type of bird: ")
    riah = input("Enter a room in a house: ")
    verb = input("Enter a verb(past tense): ")
    verb1 = input("Enter a verb: ")
    name = input("Enter a relative's name: ")
    noun = input("Enter a noun: ")
    liq = input("Enter a liquid: ")
    verb2 = input("Enter a verb ending in -ing: ")
    body = input("Enter a part of the body(plural): ")
    noun1 = input("Enter a plural noun: ")
    verb3 = input("Enter a verb ending in -ing: ")
    noun2 = input("Enter a noun: ")

    print(f"It was a {adj},cold November day. \n"
          f"I woke up to the {adj1} smell of {tib} roasting in the {riah} downstairs. \n"
          f"I {verb} down the stairs to see if I could help {verb1} the dinner. \n"
          f"My mom said, 'See if {name} needs a fresh {noun}.' \n"
          f"So I carried a tray of glasses full of {liq} into the {verb2} room. \n"
          f"When I go there, I couldn't believe my {body}! \n"
          f"There were {noun1} {verb3} on the {noun2}!")



def play():

    game_over = False
    choice = input("Which story do you want? 'story1' or 'story2' ")

     while not game_over:
        if choice == "story1":
            stroy1()
            return
        
        elif choice == "story2":
            story2()
            return

        elif choice != "story1":
            return



while input("Do you want to play ? 'y' or 'n' ") == 'y':
    play()






