#Sigurður Ingi Brynjarsson og Björn Falk Arnoldsson
#22.11.2017

#Valmynd

import random

svar = "já"

while svar == "já":
    print("")
    print("------------------")

    print("1. Fótboltalið")
    print("2. Þversumma")
    print("3. Skæri, blað, steinn")
    print("4. Texti")
    print("5. Heiltölur")
    print("6. Teningaspilið Craps//VIB -------Björn")
    print("7. Þyngadrstuðull")
    print("8. Teningar//VIB --------- Siggi")
    print("9. Byggingaupplýsingar úr Hópverkefni 1//VIB")
    print("10. Hætta")

    print("------------------")

    val = int(input("sláðu inn havð þig langar að gera:"))

    if val == 1:
        fjoldiÞatttakanda = int(input("Hvað eru margir þátttakendur?"))
        fjoldiILidi = int(input("Hvað Mikið á að vera í lið?"))

        if fjoldiÞatttakanda < fjoldiILidi:
            print("Þetta eru ekki nóg í lið")
        else:
            lidaFjoldi = int(fjoldiÞatttakanda / fjoldiILidi)
            afgangsFjoldi = fjoldiÞatttakanda % fjoldiILidi

            print("Liðafjöldi:",lidaFjoldi)
            print("Varamenn:",afgangsFjoldi)

    if val == 2:
        pass
        talaNotanda = int(input("Sláðu inn tölu sem þú villt:")) #5


        for x in range(1, talaNotanda+1, 1):
            print(x)


    if val == 3:
        svar = "ja"

        whileTeljari = 0

        tolvaVann = 0
        notandiVann = 0
        jafntefli = 0

        while svar == "ja":
            print("------------------")
            print("1. Skæri")
            print("2. Blað")
            print("3. Steinn")
            print("4. Hætta")

            val = int(input("Sláðu inn hvað þig langar:"))
            print("------------------")

            tolvaVelurRandom = random.randint(1,3)

            print("Þú settir inn",val)
            print("Tölvann setti inn",tolvaVelurRandom)
            print("------------------")

            #Skæri
            if val == 1 and tolvaVelurRandom == 2:
                print("Notandi Vann!")
                notandiVann = notandiVann + 1
            if val == 1 and tolvaVelurRandom == 3:
                print("Tölva Vann!")
                tolvaVann = tolvaVann + 1

            #Blað
            if val == 2 and tolvaVelurRandom == 3:
                print("Notandi Vann!")
                notandiVann = notandiVann + 1
            if val == 2 and tolvaVelurRandom == 1:
                print("Tölva Vann!")
                tolvaVann = tolvaVann + 1

            #Steinn
            if val == 3 and tolvaVelurRandom == 1:
                print("Notandi Vann!")
                notandiVann = notandiVann + 1
            if val == 3 and tolvaVelurRandom == 2:
                print("Tölva Vann!")
                tolvaVann = tolvaVann + 1

            #Jafntefli
            if val == tolvaVelurRandom:
                print("Jafntefli")
                jafntefli = jafntefli + 1

            whileTeljari = whileTeljari + 1

            print("Notandi vann", notandiVann, "sinnum")
            print("Tölvan vann", tolvaVann, "sinnum")
            print("Það var Jafntefli", jafntefli, "sinnum")
            print("Þetta er búið að run-a", whileTeljari, "sinnum")

    if val == 4:
        textifranotandaL3 = input("Skrifaðu texta fyrir mig:")
        textifyrirL3 = textifranotandaL3
        lengdL3 = len(textifyrirL3)

        leitarordL3 = "n"
        for c in range(0, len(textifyrirL3)):
            if textifyrirL3[c] == leitarordL3:
                print(textifyrirL3[c], end="")
            elif textifyrirL3[c] == "J":
                print("J", end="")
            elif textifyrirL3[c] == "j":
                print("j", end="")
            elif textifyrirL3[c] == "b":
                print("b", end="")
            elif textifyrirL3[c] == "l":
                print("l", end="")
            elif textifyrirL3[c] == " ":
                print("_", end="")
            else:
                print("*", end="")

    if val == 5:
        heiltoluListi = []
        summa = 0
        teljari = 12
        for x in range(12):
            print("Sláðu inn", teljari, "heiltölur")
            tolurNotanda = int(input("----> :"))

            summa = summa + tolurNotanda

            heiltoluListi.append(tolurNotanda)
            teljari = teljari - 1

        medaltal = summa / 12

        print("Summa allra talnanna:", summa)
        print("Minnsta talan:", min(heiltoluListi))
        print("Hæðsta talan:", max(heiltoluListi))
        print("Meðaltal talnanna:", medaltal)

    if val == 6:
        pass

    if val == 7:
        nafnNotanda = input("Hvað heitir þú?:")
        kynNotanda = input("Hvaða kyn ertu?( KK/KVK ):")
        þyngdNotanda = int(input("Hve þung/ur eru í kílóum:"))
        haedNotanda = float(input("Sláðu inn hæð þína í metrum:"))

        bmiHaedNotanda = haedNotanda*haedNotanda
        bmiutkommaNotanda = þyngdNotanda/bmiHaedNotanda

        tveirstafitBIMUtkomma = round(bmiutkommaNotanda, 2)

        print("BMI stuðull þinn er", tveirstafitBIMUtkomma)

        if tveirstafitBIMUtkomma < 18.5:
            print("Hærðu þú verður að borða einhvað því þetta er Vannæring", nafnNotanda)
        elif tveirstafitBIMUtkomma > 18.5 and tveirstafitBIMUtkomma < 24.99:
            print("Þú ert í kjörþynd", nafnNotanda, "yay!")
        elif tveirstafitBIMUtkomma > 25 and tveirstafitBIMUtkomma < 29.99:
            print("Hærðu nú ú ættir að skokka á hverjum mánudagi", nafnNotanda)
        elif tveirstafitBIMUtkomma > 30:
            print("Hærðu nú þú verður að hreyfa þig meira", nafnNotanda)

    if val == 8:
        pass

    if val == 9:
        pass

    if val == 10:
        print("Okey takk fyrir að not forritið okkar")
        break
