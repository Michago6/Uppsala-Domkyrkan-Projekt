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
    location["openInv"] = [["öppna","se","kolla","titta","open","opn"],[],["ryggsäck", "ryggsäcken","inv","inventory"],[]]
    for action in location:
        verbExists = False
        adjectiveExists = False
        nounExists = False
        freeFromForbiddenWords = True
        for valueIndex in range(4):
            for word in stringToList(input):
                for item in location[action][valueIndex]:
                    if word == item:
                        if valueIndex == 0:
                            verbExists = True
                        elif valueIndex == 1:
                            adjectiveExists = True
                        elif valueIndex == 2:
                            nounExists = True
                        elif valueIndex == 3:
                            freeFromForbiddenWords = False
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
def splash():
    print(r"""
----------------------------------------------------------------------------------------------------------------------------------------

  ▄   █ ▄▄  █ ▄▄    ▄▄▄▄▄   ██   █    ██       ██▄   ████▄ █▀▄▀█ █  █▀ ▀▄    ▄ █▄▄▄▄ █  █▀ ██      ▄                     _|_
   █  █   █ █   █  █     ▀▄ █ █  █    █ █      █  █  █   █ █ █ █ █▄█     █  █  █  ▄▀ █▄█   █ █      █                     |
█   █ █▀▀▀  █▀▀▀ ▄  ▀▀▀▀▄   █▄▄█ █    █▄▄█     █   █ █   █ █ ▄ █ █▀▄      ▀█   █▀▀▌  █▀▄   █▄▄█ ██   █                   _|_
█   █ █     █     ▀▄▄▄▄▀    █  █ ███▄ █  █     █  █  ▀████ █   █ █  █     █    █  █  █  █  █  █ █ █  █                  //_/\
█▄ ▄█  █     █                 █     ▀   █     ███▀           █    █    ▄▀       █     █      █ █  █ █                __|  ||____
 ▀▀▀    ▀     ▀               █         █                    ▀    ▀             ▀     ▀      █  █   ██               ////////////\
                        █   █ ▀         ▀                                                    ▀                      /////////////\\ 
▄███▄     ▄▄▄▄▀ ▄▄▄▄▀     ██       ▄   ▄███▄      ▄     ▄▄▄▄▀ ▀▄    ▄ █▄▄▄▄   ▄▄▄▄▄    ▄▄▄▄▄   █ ▄▄  ▄███▄   █      |^^^^^^^^^^||+|
█▀   ▀ ▀▀▀ █ ▀▀▀ █        █ █       █  █▀   ▀      █ ▀▀▀ █      █  █  █  ▄▀  █     ▀▄ █     ▀▄ █   █ █▀   ▀  █      |  # # #   ||||
██▄▄       █     █        █▄▄█ █     █ ██▄▄    ██   █    █       ▀█   █▀▀▌ ▄  ▀▀▀▀▄ ▄  ▀▀▀▀▄   █▀▀▀  ██▄▄    █       ....    ....".
█▄   ▄▀   █     █         █  █  █    █ █▄   ▄▀ █ █  █   █        █    █  █  ▀▄▄▄▄▀   ▀▄▄▄▄▀    █     █▄   ▄▀ ███▄   |||||||||||||||||
▀███▀    ▀     ▀             █   █  █  ▀███▀   █  █ █  ▀       ▄▀       █                       █    ▀███▀       ▀ 
                            █     █▐           █   ██                  ▀                         ▀                 
                           ▀      ▐                                                                                

----------------------------------------------------------------------------------------------------------------------------------------
    """)
    name = input("Skriv ditt namn: ")
    print(f"Hej {name}, välkommen till Uppsala! Jag heter Karl och vi befinner oss just nu i domkyrkan i mitten av staden. Året är 1500 och vintern närmar sig. Jag är en föreläsare på Uppsala\nuniversitet och jag undervisar i datavetenskap tillsammans med min kollega Aletta. Just nu är Aletta väldigt arg på mig och vägrar prata med mig eftersom jag lämnade henne själv igår på\nvår gemensamma föreläsningen så att hon behövde presentera mina slides. Skulle du kunna prata med henne och få henne att förlåta mig?\n")
    return name

def openInv(inventory):
    if len(inventory) == 0:
        print("Din ryggsäck är tom")
    else:
        print("I din ryggsäck ser du ", end="")
    for item in inventory:
        print(f"{item} ",end="")
        print()

def levelOne(inventory):
    print("Du är i domkyrkan.")
    pos = "karl"
    while True:
        playerInput = input("Vad vill du göra? -> ")
        action = determineAction(playerInput, actionsA1)
        if action == "openInv":
            openInv(inventory)
        elif action == "talkToAletta":
            if pos == "aletta":
                print(f"Hej {name}! Jag såg att du pratade med Karl. Hälsa att jag fortfarande är arg på honom om du återvänder till honom.\nMen men... det är bra att du är här. Det är så att jag har glömt min plånbok i aulan av universitetshuset och det hade gjort mig glad om du kunde hitta och återlämna den till mig.\n Du låna min häst för att ta dig dit. Ta denna karta, den kommer att leda dig till universitetshuset.\n(Kolla nu i din ryggsäck så borde du se kartan)")
                inventory.append("en karta")
            else:
                print("Du försöker prata med Aletta men hon står på andra sidan av salen.")
        elif action == "goToAletta":
            if pos == "aletta":
                print("Du är redan vid Aletta och hon stirrar dig i ögonen, ner in i din själ...")
            else:
                pos = "aletta"
                print("Du går till Aletta och du har nu hennes uppmärksamhet.")
        elif action == "takeTheHorseToLvlTwo":
            if pos == "horse":
                if "en karta" in inventory:
                    print("Du tar hästen och rider till universitetshuset\n")
                    print("Du står framför två stora dörrar som leder in i byggnaden, ena dörren verkar stå på glänt.")
                    levelTwo(inventory)
                    break
                else:
                    print("Du kan inte vägen till universitetshuset...")
            else:
                print("Hästen är för långt bort, pröva gå till hästen.")
        elif action =="takeTheHorseAndGetLost":
            if pos == "horse":
                print("Du tog hästen men tappade bort dig i stan då du inte hade en destination. Du rider tillbaka till domkyrkan ur desperation... Testa ange din destination.")
            else:
                print("Hästen är för långt bort, pröva gå till hästen.")

        elif action == "goToHorse":
            if pos == "horse":
                print("Du kliver tre millimeter närmare hästen. Hästen ger dig en konstig blick...")
            else:
                print("Du står nu brevid hästen vid entrén av domkyrkan.")
                pos = "horse"
        elif action == "aletta":
            print("Aletta vinkar till dig.")
        elif action == "karl":
            print("Karl fipplar med något i handen, du ser inte vad...")
        else:
            print("Inget hände...")
        print()
def levelTwo(inventory):
    print("Du är vid entrén av universitetshuset.")
    pos = "entrance"
    while True:
        playerInput = input("Vad vill du göra? -> ")
        action = determineAction(playerInput, actionsA2)
        match action:
            case "openInv":
                openInv(inventory)
            case "enter":
                print("Du går in i universitetshuset och befinner dig nu i aulan där det sker en föreläsning om bibelkunskap.")
            case _:
                print("Inget hände...")
        print()
                
        
#Globala variabler:
inventory = []
actionsA1 = {
    "talkToAletta":[["snacka","prata","tala"],[],["aletta"],["inte"]],
    "goToAletta":[["gå"],[],["aletta"],["inte"]],
    "takeTheHorseToLvlTwo":[["rida","rid","ta"],["universitetshuset"],[],["inte"]],
    "takeTheHorseAndGetLost":[["rida","rid","ta"],[],[],["inte"]],
    "goToHorse":[["gå"],[],["häst","hästen"],["inte"]],
    "aletta":[[],[],["aletta"],[]],
    "karl":[[],[],["karl"],[]]
    }
actionsA2 = {
    "enter":[["gå"],["in"],[],[]]
    }
#actionsA_ = {"action_name":[[verbs],[adjectives],[nouns],[forbiddenwords]]}

#Copy paste add action:
#,"":[["",""],[""],[""],[""]]

#Run
name = splash()
levelOne(inventory)

