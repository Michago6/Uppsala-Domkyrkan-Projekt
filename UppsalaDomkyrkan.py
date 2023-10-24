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
    location["openMap"] = [["öppna","se","kolla","titta","open","opn","ta","använd"],[],["map","karta","kartan"],[]]
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
    print(f"\nHej {name}, välkommen till Uppsala! Jag heter Karl och vi befinner oss just nu i domkyrkan i mitten av staden. Året är 1500 och vintern närmar sig. Jag är en föreläsare på Uppsala universitet och jag undervisar i datavetenskap tillsammans med min kollega Aletta. Just nu är Aletta väldigt arg på mig och vägrar prata med mig eftersom jag lämnade henne själv igår på vår gemensamma föreläsningen så att hon behövde presentera mina slides. Skulle du kunna prata med henne och få henne att förlåta mig?\n")
    return name

def openInv(inventory):
    if len(inventory) == 0:
        print("Din ryggsäck är tom")
    else:
        print("I din ryggsäck ser du följande föremål: ", end="")
    for item in inventory:
        print(f"{item}, ",end="")
def openMap(inventory):
    if "en karta" in inventory:
        print(r"""                                                                                                        
       █████████▄█████████▄                                  
     ███       ██°°°°°   ███▄▄▄   ██████████████████▄        
     █    ▲ ▲  ▲     ▲     °███████░░░~       N     ██       
     ██   ▀ ▀  ▀     ▀            ~░~~░~      ▲     ██       
      ██  ░░░░░░░ ▲ ░░            ~░░~░░░~ W◄   ►E   █       
       █  ░ ▲   ░░▀ ░ ░▲           ~░░┼~░░┼   ▼      █       
      ██  ▲ ▀     ░░░ ░▀            ~░█~~~█░░~S      █       
      █   ▀         ▲ ░░          ┼  ~█░░░█~░▓▓▓     ██      
     ██             ▀             █▄▄█▒█~█▒█~▓░░~~~   █      
     █     ▄▄▄▄▄▄▄▄              █████▒█ █▒█▓▓~░░░░~  █▄     
    ██▄▄▄▄▄▄█▄▄▄▄█▄▄▄▄▄▄▄       ██████▒█ █▒█▓░░~~░░░░~██▄    
    █ ▐▓▓▓▓▓█▓▓▓▓█▓▓▓▓▓▌       █▒▒███▒▒▒█▒♀█~ ░░░~~~░░░██    
   █  ▐▒▒╬▒╬█╬▒▒╬█╬▒╬▒▒▌     ▓█▒▒╫╫▒█████▒▒▒█   ░░░~ ~░░█    
    █▐█▄▀▀▀▀▓▀▀▀▀▓▀▀▀▀▄█▌    ▓█▓▒▒▒█▒▒╫╫▒█▒▒█      ░░~~~█    
    █▐▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▌▓      ▓▓▓█▒▒▒▒▒▒█∩▓       ░░░░█    
    █▐▒▒▒╬▒╬▓╬▓▓╬▓╬▒╬▒▒▒▌▓          ▓▓▓▓▓▓█▓■         ░░█▄   
    █▓▀▀▒▒▒▒▓▓∩∩▓▓▒▒▒▒▀▀▓               ■  ■          ░░██   
    █▓▓▓▀▀▀▀██▀▀██▀▀▀▀▓▓           ■  ■          ▲     ░░█   
    █   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓           ■               ▀    ▲ ██   
    ██      ▓▓▓▓▓▓                               ░░▲  ▀██▓   
     ███     ▓▓▓▓■      ■  ■     ■            ▲ ░ ░▀ ░░█▓    
      ▀▀██°        ■  ■     ■   ■             ▀░   ░░  █▓    
         ███                 ▄■    °  °       ░░ ███████     
           ▀█████ °     ████████  °°°° °     ████▓▓▓▓▓▓      
              ▀▀▀███████    ▀▀▀████°°° ███████▓▓▓            
                    ▀▀          ▀▀█████▓▓▓▓▓▓▓                          
        """)
    else:
        print("Du har ingen karta...")

def levelOne(inventory):
    print("Du är i domkyrkan.")
    pos = "karl"
    while True:
        playerInput = input("Vad vill du göra? -> ")
        action = determineAction(playerInput, actionsA1)
        if action == "openInv":
            openInv(inventory)
        elif action == "openMap":
            openMap(inventory)
        elif action == "talkToAletta":
            if pos == "aletta":
                if "Alettas plånbok" in inventory:
                    print(f"Tack {name} för all din hjälp, jag är evigt tacksam för att du hittat min plånbok! Som tack vill jag erbjuda dig tio riksdaler.\n(Kolla nu i din ryggsäck så borde du se tio riksdaler)")
                    inventory.append("10rdr")
                    inventory.remove("Alettas plånbok")
                else:
                    print(f"Hej {name}! Jag såg att du pratade med Karl. Hälsa att jag fortfarande är arg på honom om du återvänder till honom.\nMen men... det är bra att du är här. Det är så att jag har glömt min plånbok i aulan av universitetshuset och det hade gjort mig glad om du kunde hitta och återlämna den till mig.\n Du kan låna min häst för att ta dig dit. Ta denna karta, den kommer att leda dig till universitetshuset.\n(Kolla nu i din ryggsäck så borde du se kartan)")
                    inventory.append("en karta")
            else:
                print("Du försöker prata med Aletta men hon står på andra sidan av salen.")
        elif action == "giveWalletToAletta":
            if "Alettas plånbok" in inventory:
                print(f"Tack {name} för all din hjälp, jag är evigt tacksam för att du hittat min plånbok! Som tack vill jag erbjuda dig tio riksdaler.\n(Kolla nu i din ryggsäck så borde du se tio riksdaler)")
                inventory.append("10rdr")
                inventory.remove("Alettas plånbok")
            else:
                print("Du har inte Alettas plånbok.")
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
    pos = "vid entrén"
    while True:
        playerInput = input("Vad vill du göra? -> ")
        action = determineAction(playerInput, actionsA2)
        match action:
            case "openInv":
                openInv(inventory)
            case "openMap":
                openMap(inventory)
            case "goToJohan":
                print(f"Hey {name} how fun to see you here at the bible lecture! If theres anything I can do for you just tell me.")
                pos = "vid johan"
            case "enter":
                if pos != "aulan":
                    print("Du går in i universitetshuset och befinner dig nu i aulan där det sker en föreläsning om bibelkunskap.")
                    pos = "aulan"
                else:
                    print("Du står i aulan.")
            case "goToHorse":
                if pos == "vid hästen":
                    print("Du kliver tre millimeter närmare hästen. Hästen ger dig en konstig blick...")
                else:
                    print("Du står nu brevid hästen vid entrén av domkyrkan.")
                    pos = "vid hästen"
            case "goToReception":
                print(f"Hej {name} välkommen till expeditionen, hur kan jag hjälpa er?")
                pos = "i expeditionen"
            case "plånbok":
                if pos == "aulan":
                    print("Du letar hektiskt i aulan men hittar inte plånboken... Men på föreläsningen ser du lärarassistenten Johan Snider, gå till honom och fråga om han har sett Alettas plånbok.")
                elif pos == "vid johan":
                    print("Unfortunately I haven't seen Aletta's wallet, I suggest asking the reception if they retreived a wallet.")
                elif pos == "i expeditionen":
                    if "Alettas plånbok" in inventory:
                        print("Du har redan fått Alettas plånbok.")
                    else:
                        print("Ja, vi har fått in en plånbok med Alettas namn på. Var så god och ta den!\n(Kolla nu i din ryggsäck så borde du se Alettas plånbok)")
                        inventory.append("Alettas plånbok")
                else:
                    if "Alettas plånbok" in inventory:
                        print(f"Du står {pos}.")
                    else:
                        print(f"Du står {pos}, gå till aulan för att leta efter plånboken.")
            case "goToDomkyrkan":
                    print("Du tar hästen och rider till domkyrkan\n")
                    levelOne(inventory)
            case _:
                print("Inget hände...")
        print()
                
        
#Globala variabler:
inventory = []
actionsA1 = {
    "talkToAletta":[["snacka","prata","tala"],[],["aletta","henne","hon"],["inte"]],
    "goToAletta":[["gå"],[],["aletta","dit","salen","närmare"],["inte"]],
    "takeTheHorseToLvlTwo":[["rida","rid","ta","åka","åk","åker","gå"],["universitetshuset","universitetsaulan"],[],["inte"]],
    "takeTheHorseAndGetLost":[["rida","rid","ta"],[],[],["inte"]],
    "goToHorse":[["gå"],[],["häst","hästen"],["inte"]],
    "giveWalletToAletta":[["ge","återlämna","ger"],["plånbok","plonkan","plånboken","plonka"],["aletta","henne","hon","tillbaka"],["inte"]],
    "aletta":[[],[],["aletta"],[]],
    "karl":[[],[],["karl"],[]]
    }
actionsA2 = {
    "plånbok":[[],[],["plånbok","plånboken","plånka","plånkan","wallet"],[]],
    "goToJohan":[["gå","snacka","prata","tala"],[],["johan","snider","han","honom"],["inte","expedition","expeditionen","receptionen","reception"]],
    "goToHorse":[["gå"],[],["häst","hästen"],["inte"]],
    "goToReception":[["gå","snacka","prata","tala","besök","fråga","frågar"],[],["expeditionen","expedition","reception","receptionen"],["inte"]],
    "goToDomkyrkan":[["gå","rid","rida","häst","hästen","återvänd","åk"],[],["domkyrkan","aletta","karl","domkyrka","kyrka","kyrkan","tillbaka"],[]],
    "enter":[["gå","öppna","dörr","dörren"],[],[],["ryggsäck","ryggsäcken","inv","inventory","säcken","karta","kartan","map"]]
    }
#actionsA_ = {"action_name":[[verbs],[adjectives],[nouns],[forbiddenwords]]}

#Copy paste add action:
#,"":[["",""],[""],[""],[""]]

#Run
name = splash()
levelOne(inventory)

