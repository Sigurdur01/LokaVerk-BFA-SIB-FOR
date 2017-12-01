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
    print("6. Teningaspilið Craps")
    print("7. Þyngadrstuðull")
    print("8. Teningar")
    print("9. Byggingaupplýsingar úr Hópverkefni 1")
    print("10. Hætta")

    print("------------------")

    val = int(input("Sláðu inn hvað þig langar að gera:"))

    if val == 1:
        #Hér er spurt um innsláningu frá notanda
        fjoldiÞatttakanda = int(input("Hvað eru margir þátttakendur?"))
        fjoldiILidi = int(input("Hvað Mikið á að vera í lið?"))

        #Hér er Sjéð hvort það eru nóg af fólki í lið
        if fjoldiÞatttakanda < fjoldiILidi:
            #Ef það er ekki nóg af leikmönnum í of stórt lið
            print("Þetta eru ekki nóg í lið")
        else:
            lidaFjoldi = int(fjoldiÞatttakanda / fjoldiILidi)
            afgangsFjoldi = fjoldiÞatttakanda % fjoldiILidi

            #Hér er prentaður Liðafjöldi og afgangur
            print("Liðafjöldi:",lidaFjoldi)
            print("Varamenn:",afgangsFjoldi)

    if val == 2:
        keyra = "já"
        while keyra == "já":
            #Hér er spurt um innsláningu frá notanda
            talaNotanda = int(input("Sláðu inn tölu sem þú villt:"))
            #Bý til breytu fyrir teljara
            teljari = 0
            #ef talanotanda er mínustala leggur hún saman í mínus
            if talaNotanda <= -1:
                for x in range(-1, talaNotanda - 1, -1):
                    print("(", x, ")", end="")
                    print("+", end="")
                    teljari = teljari - x
                print("=", - teljari, end="")
            #ef talan er 0 þá stoppar forritið
            elif talaNotanda == 0:
                break
            #ef talna er í plús þá leggur hún tölurnar saman venjulega
            else:
                for x in range(1, talaNotanda + 1):
                    print(x, end="")
                    print(" + ", end="")
                    teljari = teljari + x
                print("=", teljari, end="")
            print("")
            #spyr hvort notandi vilji keyra aftur
            keyra = input("Villtu keyra aftur já/nei")

    if val == 3:
        svarL3 = "ja"

        whileTeljari = 0

        #Telur hve oft tölvan Vinnur
        tolvaVann = 0
        #Telur hve oft notandni vinnur
        notandiVann = 0
        #Telur hve oft jafntefli kemur
        jafntefli = 0

        while svarL3 == "ja":
            print("------------------")
            print("1. Skæri")
            print("2. Blað")
            print("3. Steinn")
            print("4. Hætta")

            #Hér er spurt um innsláningu frá notanda
            valL3 = int(input("Sláðu inn hvað þig langar:"))
            print("------------------")

            #Hér er val tölvunar
            tolvaVelurRandom = random.randint(1,3)

            #Hér er spurt um innsláningu frá notanda um hvað þeim langar að nota ( skæri, blað, steinn )
            print("Þú settir inn",val)
            print("Tölvann setti inn",tolvaVelurRandom)
            print("------------------")

            #Skæri
            if valL3 == 1 and tolvaVelurRandom == 2:
                #Notandi vinnur ef talvan velur blað og notandi velur skæri
                print("Notandi Vann!")
                #Hér er bætt í teljaran þegar notandi vinnur
                notandiVann = notandiVann + 1
            if valL3 == 1 and tolvaVelurRandom == 3:
                #Tölvan vinnur ef talvan velur stein og notandi velur skæri
                print("Tölva Vann!")
                #Hér er bætt í teljaran þegar tölvan vinnur
                tolvaVann = tolvaVann + 1

            #Blað
            if valL3 == 2 and tolvaVelurRandom == 3:
                #Notandi vinnur ef talvan velur stein og notandi velur blað
                print("Notandi Vann!")
                #Hér er bætt í teljaran þegar notandi vinnur
                notandiVann = notandiVann + 1
            if valL3 == 2 and tolvaVelurRandom == 1:
                #Tölvan vinnur ef talvan velur skæri og notandi velur blað
                print("Tölva Vann!")
                #Hér er bætt í teljaran þegar tölvan vinnur
                tolvaVann = tolvaVann + 1

            #Steinn
            if valL3 == 3 and tolvaVelurRandom == 1:
                #Notandi vinnur ef talvan velur skæri og notandi velur stein
                print("Notandi Vann!")
                #Hér er bætt í teljaran þegar notandi vinnur
                notandiVann = notandiVann + 1
            if valL3 == 3 and tolvaVelurRandom == 2:
                #Tölvan vinnur ef talvan velur blað og notandi velur skæri
                print("Tölva Vann!")
                #Hér er bætt í teljaran þegar tölvan vinnur
                tolvaVann = tolvaVann + 1

            #Jafntefli
            #Séð hvort það var sett það samma inn t.d notandi velur 1 og talvan velur 1 = jafntefli
            if valL3 == tolvaVelurRandom:
                print("Jafntefli")
                #Hér er bætt við teljaran ef jantefli kemur upp
                jafntefli = jafntefli + 1

            #Hér er bætt við teljaran þegar while lykkajn fer í gegn
            whileTeljari = whileTeljari + 1

            #Hér er prentað út alla teljarana
            print("Notandi vann", notandiVann, "sinnum")
            print("Tölvan vann", tolvaVann, "sinnum")
            print("Það var Jafntefli", jafntefli, "sinnum")
            print("Þetta er búið að run-a", whileTeljari, "sinnum")

            if valL3 == 4:
                svarL3 = "nei"

    if val == 4:
        #Hér er spurt um innsláningu frá notanda
        textifranotandaL3 = input("Skrifaðu texta fyrir mig:")
        textifyrirL3 = textifranotandaL3
        lengdL3 = len(textifyrirL3)

        #Hér eru stafirnir sem við viljum geyma
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
            #Hér er ef bil er þá koma undirstrik
            elif textifyrirL3[c] == " ":
                print("_", end="")
            #Hér eru all stafirnir breyttir yfir í *
            else:
                print("*", end="")

    if val == 5:
        #Hér eru allar tölurnar sem notandi slær inn
        heiltoluListi = []
        #Hér er summa allra talna sem notandi hefur sláðið inn
        summa = 0
        #Þessi teljari er fyrir niðurtal
        teljari = 12
        #Hér er FOR lykkja sem biður um heiltölu hjá notanda
        for x in range(12):
            print("Sláðu inn", teljari, "heiltölur")
            tolurNotanda = int(input("----> :"))

            summa = summa + tolurNotanda

            #Hér er bætt inní listan allar heiltöluran
            heiltoluListi.append(tolurNotanda)
            #Hér minnkað í teljarann
            teljari = teljari - 1

        #Hér er verið að reikna meðaltal talnana
        medaltal = summa / 12

        #Hér er prenta út summu talnana
        print("Summa allra talnanna:", summa)
        #Hér er prentað minnstu töluna
        print("Minnsta talan:", min(heiltoluListi))
        #Hér er prentað hæðastu töluna
        print("Hæðsta talan:", max(heiltoluListi))
        #Hér er prentað meðaltalið
        print("Meðaltal talnanna:", medaltal)

    if val == 6:
        #breytur fá random tölu á bilinu 1 - 6 til að líkjast teningum
        teningur1 = random.randint(1, 6)
        teningur2 = random.randint(1, 6)

        #breyta telur stig notanda
        stig = 0
        #summa random talnanna
        summa = teningur1 + teningur2
        print("------------------")
        print("Summa er", summa)
        #ef summan er 7 eað 11 í fyrsta kasti vinnur leikmaður
        if summa == 7 or summa == 11:
            print("------------------")
            print("Leikmaður vinnur")
        #ef summa er 2, 3 eða 12 vinnur húsið
        elif summa == 2 or summa == 3 or summa == 12:
            print("------------------")
            print("Husið vinnur")
        #ef summan er einhver önnur tala þá verður sá tala stig notanda
        else:
            nySumma = 0
            #bættir summu úr fyrsta kasti í stig notanda
            stig = stig + summa
            #"teningum" er kastað aftur og aftur þangatil að notandi fær sömu tölu og stig notanda
            while nySumma != stig:
                teningur1 = random.randint(1, 6)
                teningur2 = random.randint(1, 6)

                nySumma = teningur1 + teningur2
                print("Summa Kast", nySumma)
                #ef summa er 7 þá vinnur húsið
                if nySumma == 7:
                    print("------------------")
                    print("húsið vinnur")
                    break
                #ef notandi fær sömmu tölu og hann fékk í fyrsta kasti vinnur notandi
                elif nySumma == stig:
                    print("------------------")
                    print("leikmaður vinnur")
                    print("Summa", nySumma)
            print("stig", stig)

    if val == 7:
        #Hér er spurt um innsláningu frá notanda
        nafnNotanda = input("Hvað heitir þú?:")
        kynNotanda = input("Hvaða kyn ertu?( KK/KVK ):")
        þyngdNotanda = int(input("Hve þung/ur eru í kílóum:"))
        haedNotanda = float(input("Sláðu inn hæð þína í metrum:"))

        #Hér er sett hæð notanda í annað veldi
        bmiHaedNotanda = haedNotanda*haedNotanda
        #Hér er deilt þyngd með hæð í öðru veldi
        bmiutkommaNotanda = þyngdNotanda/bmiHaedNotanda

        #Hér er breytt töluni til að bara hafa tvo aukastafi
        tveirstafitBIMUtkomma = round(bmiutkommaNotanda, 2)

        print("BMI stuðull þinn er", tveirstafitBIMUtkomma)

        #Hér er séð hvað BMI stuðullin þinn er við inna áhvaða marka
        if tveirstafitBIMUtkomma < 18.5:
            print("Hærðu þú verður að borða einhvað því þetta er Vannæring", nafnNotanda)
        elif tveirstafitBIMUtkomma > 18.5 and tveirstafitBIMUtkomma < 24.99:
            print("Þú ert í kjörþynd", nafnNotanda, "yay!")
        elif tveirstafitBIMUtkomma > 25 and tveirstafitBIMUtkomma < 29.99:
            print("Hærðu nú ú ættir að skokka á hverjum mánudagi", nafnNotanda)
        elif tveirstafitBIMUtkomma > 30:
            print("Hærðu nú þú verður að hreyfa þig meira", nafnNotanda)

    if val == 8:
        listiTeningarKastL8 = []
        listiFyrirSummurL8 = []

        heildarSummaListans = 0

        teljariFyrir10L8 = 0
        teljariFyrir15L8 = 0
        teljariFyrir18L8 = 0


        for x in range(201):
            randomTeningarKastL8_1 = random.randint(1,6)
            randomTeningarKastL8_2 = random.randint(1,6)
            randomTeningarKastL8_3 = random.randint(1,6)

            summaAllraTalnaL8 = randomTeningarKastL8_1 + randomTeningarKastL8_2 + randomTeningarKastL8_3
            heildarSummaListans = heildarSummaListans + summaAllraTalnaL8

            print("Kast teningur 1 =", randomTeningarKastL8_1)
            print("Kast teningur 2 =", randomTeningarKastL8_2)
            print("Kast teningur 3 =", randomTeningarKastL8_3)

            print("Samtals",summaAllraTalnaL8)

            listiFyrirSummurL8.append(summaAllraTalnaL8)

            listiTeningarKastL8.append(randomTeningarKastL8_1)
            listiTeningarKastL8.append(randomTeningarKastL8_2)
            listiTeningarKastL8.append(randomTeningarKastL8_3)

            if heildarSummaListans == 10:
                teljariFyrir10L8 = teljariFyrir10L8 + 1
            if heildarSummaListans == 15:
                teljariFyrir15L8 = teljariFyrir15L8 + 1
            if heildarSummaListans == 18:
                teljariFyrir18L8 = teljariFyrir18L8 + 1

            print("------------------")

        print("Hér er listinn óraðaður:")
        print(listiTeningarKastL8)

        print("------------------")

        listiTeningarKastL8.sort()
        print("Hér er listinn raðaður:")
        print(listiTeningarKastL8)

        print("------------------")

        print("Hér er heildarsumma listans:", heildarSummaListans)

        print("------------------")

        medaltalL8 = heildarSummaListans / 200
        print("Þetta er meðaltal kastanna", medaltalL8)

        print("------------------")

        print("Kastað var uppá 10", teljariFyrir10L8, "sinnum")
        print("Kastað var uppá 15", teljariFyrir15L8, "sinnum")
        print("Kastað var uppá 18", teljariFyrir18L8, "sinnum")

        print("------------------")

    if val == 9:
        byggingar = ["Kyrkja","Listasafn"]
        stadsetning = ["Skólavörðuholti","Kjarvalsstaðir"]
        arkitektar = ["Guðjón Samúelsson","Hannes Kr. Davíðsson"]
        byggingarAr = ["1986","1973"]

        print("------------------")

        print("1. Hallgrímskyrkju")
        print("2. Kjarvalsstaði")

        print("------------------")

        valL9 = input("Hvað byggingu langar þér að læra um?:")

        if valL9 == "1":
            print("------------------")

            print("Heimilsfang byggingar:  ",stadsetning[0])
            print("Arkitekt:               ",arkitektar[0])
            print("Byggingarár:            ",byggingarAr[0])

        elif valL9 == "2":
            print("------------------")

            print("Heimilsfang byggingar:  ",stadsetning[1])
            print("Arkitekt:               ",arkitektar[1])
            print("Byggingarár:            ",byggingarAr[1])
        else:
            print("Villa!")

    if val == 10:
        print("Okey takk fyrir að not forritið okkar")
        break
