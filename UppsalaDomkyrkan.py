def stringToList(phrase):
    #Funktionen tar ditt svar, separerar springen till en lista med alla ord i din mening
    #listan är kronologisk, första ord till sista ord
    #Gör alla orden till lower case.
    #non-bokstäver karaktärer tas inte med! (#, !, .)
    lst=[]
    strng = []
    forbiddenChars =["!",".",",","?"]
    phrase = phrase + " "
    for item in phrase:
        if item == " ":
            ord=""
            for letter in strng:
                ord=ord+letter.lower()
            lst.append(ord)
            strng.clear()
        elif item in forbiddenChars:
            pass
        else:
            strng.append(item)
    return lst

def determineAction(input, location):
    verbExists = False
    adjectiveExists = False
    nounExists = False
    freeFromForbiddenWords = True
    for action in location: 
        for valueIndex in range(4):
            for word in stringToList(input):
                for item in location[action][valueIndex]:
                    if word == item:
                        if valueIndex == 0:
                            verbExists = True
                            break
                        elif valueIndex == 1:
                            adjectiveExists = True
                            break
                        elif valueIndex == 2:
                            nounExists = True
                            break
                        elif valueIndex == 3:
                            freeFromForbiddenWords = False
                            break
        retAction = True
        if len(location[action][0]) != 0 and verbExists == False:
            retAction = False
        elif len(location[action][1]) != 0 and adjectiveExists == False:
            retAction = False
        elif len(location[action][2]) != 0 and nounExists == False:
            retAction = False
        elif len(location[action][3]) != 0  and freeFromForbiddenWords == False:
            retAction = False
        if retAction:
            return action
        else:
            return "Nothing Happened"

def splash():
    print(r"""\


  ▄   █ ▄▄  █ ▄▄    ▄▄▄▄▄   ██   █    ██       ██▄   ████▄ █▀▄▀█ █  █▀ ▀▄    ▄ █▄▄▄▄ █  █▀ ██      ▄               
   █  █   █ █   █  █     ▀▄ █ █  █    █ █      █  █  █   █ █ █ █ █▄█     █  █  █  ▄▀ █▄█   █ █      █              
█   █ █▀▀▀  █▀▀▀ ▄  ▀▀▀▀▄   █▄▄█ █    █▄▄█     █   █ █   █ █ ▄ █ █▀▄      ▀█   █▀▀▌  █▀▄   █▄▄█ ██   █             
█   █ █     █     ▀▄▄▄▄▀    █  █ ███▄ █  █     █  █  ▀████ █   █ █  █     █    █  █  █  █  █  █ █ █  █             
█▄ ▄█  █     █                 █     ▀   █     ███▀           █    █    ▄▀       █     █      █ █  █ █             
 ▀▀▀    ▀     ▀               █         █                    ▀    ▀             ▀     ▀      █  █   ██             
                        █   █ ▀         ▀                                                    ▀                      
▄███▄     ▄▄▄▄▀ ▄▄▄▄▀     ██       ▄   ▄███▄      ▄     ▄▄▄▄▀ ▀▄    ▄ █▄▄▄▄   ▄▄▄▄▄    ▄▄▄▄▄   █ ▄▄  ▄███▄   █     
█▀   ▀ ▀▀▀ █ ▀▀▀ █        █ █       █  █▀   ▀      █ ▀▀▀ █      █  █  █  ▄▀  █     ▀▄ █     ▀▄ █   █ █▀   ▀  █     
██▄▄       █     █        █▄▄█ █     █ ██▄▄    ██   █    █       ▀█   █▀▀▌ ▄  ▀▀▀▀▄ ▄  ▀▀▀▀▄   █▀▀▀  ██▄▄    █     
█▄   ▄▀   █     █         █  █  █    █ █▄   ▄▀ █ █  █   █        █    █  █  ▀▄▄▄▄▀   ▀▄▄▄▄▀    █     █▄   ▄▀ ███▄  
▀███▀    ▀     ▀             █   █  █  ▀███▀   █  █ █  ▀       ▄▀       █                       █    ▀███▀       ▀ 
                            █     █▐           █   ██                  ▀                         ▀                 
                           ▀      ▐                                                                                


    """)
    name = input("skriv ditt namn: ")
    return name
    
name = splash()

def levelOne():
    print(f"Välkommen till domkyrkan {name}. Börja med att prata med Aletta för att få ditt första uppdrag.")
    playerInput = input("Vad vill du göra? ")
    
    if determineAction(playerInput, actionsA1) == "goToAletta":
        print("Du gick till Aletta")
    else:
        print(determineAction(playerInput, actionsA1))
    
    playerInput = input("Vad vill du göra? ")

    if determineAction(playerInput, actionsA1) == "goToAletta":
        print("Du pratade med Aletta")
    else:
        print(determineAction(playerInput, actionsA1))

actionsA1 = {"talkToAletta":[["snacka","prata","tala"],[],["aletta"],["inte"]]}
# actionsA_ = {"action_name":[[verbs],[adjectives],[nouns],[forbiddenwords]]}
