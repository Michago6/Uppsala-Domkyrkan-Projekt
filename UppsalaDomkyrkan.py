print("Hello Uppsala")

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
