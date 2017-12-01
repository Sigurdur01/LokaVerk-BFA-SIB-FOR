#Sigurður Ingi Brynjarsson og Björn Falk Arnoldsson
#22.11.2017

#Valmynd

import random

svar = "já"

while svar == "já":
    print("1. Fótboltalið")
    print("2. Þversumma//VIB")
    print("3. Skæri, blað, steinn")
    print("4. Texti")
    print("5. Heiltölur")
    print("6. Teningaspilið Craps")
    print("7. Þyngdarstuðull")
    print("8. Teningar")
    print("9. Byggingarupplýsingar")
    print("10. Hætta")

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
        keyra = "ja"
        while keyra == "ja":
            talaNotanda = int(input("Sláðu inn tölu sem þú villt:")) #5
            teljari = 0

            if talaNotanda <= -1:
                for x in range(-1, talaNotanda-1,-1):
                    print("(",x,")" ,end="")
                    print("+",end="")
                    teljari = teljari - x
                print("=",- teljari, end="")
            elif talaNotanda == 0:
                break
            else:
                for x in range(1, talaNotanda + 1):
                    print(x, end="")
                    print(" + ", end="")
                    teljari = teljari + x
                print("=", teljari, end="")
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
        pass

    if val == 5:
        pass

    if val == 6:
        teningur1 = random.randint(1,6)
        teningur2 = random.randint(1,6)

        stig = 0
        summa = teningur1 + teningur2

        print("Summa er",summa)
        if summa == 7 or summa == 11:
            print("Leikmaður vinnur")
        elif summa == 2 or summa == 3 or summa == 12:
            print("Husið vinnur")
        else:
            nySumma = 0
            stig = stig + summa
            while nySumma != stig:
                teningur1 = random.randint(1, 6)
                teningur2 = random.randint(1, 6)

                nySumma = teningur1 + teningur2
                print("Summa Kast", nySumma)
                if nySumma == 7:
                    print("húsið vinnur")
                    break
                elif nySumma == stig:
                    print("leikmaður vinnur")
                    print("Summa",nySumma)
            print("stig",stig)


    if val == 7:
        pass

    if val == 8:
        pass

    if val == 9:
        pass

    if val == 10:
        print("Oeky takk fyrir að not forritið okkar")
        break