question = input("Välkommen till BlackJack! Vet du hur man spelar? Ja eller Nej?  ")
if question == "Ja":
    print("Vad bra! Då börjar vi!")
elif question == "Nej":
    print("Det är okej, här kommer några regler: ")
    print("Du kommer få två kort och jag, dealern, kommer få två kort. Du får be om så många kort som du vill, målet är att få högre än mig. Om du däremot får högre än 21 så förlorar du direkt. Förstår du? ")
    regler = input("Ja eller Nej?: ")
    if regler == "Ja":
        print("Vad bra då spelar vi!")
    elif question == "Nej":
        print("Det är okej, här kommer dom igen: ")
        print("Du kommer få två kort och jag, dealern, kommer få två kort. Du får be om så många kort som du vill, målet är att få högre än mig. Om du däremot får högre än 21 så förlorar du direkt. ")
        print("Nu hoppas jag att du förstår för nu ska vi köra!")

def main():
    spela = input("Då ska vi sätta igång! Skriv 'Starta' för att sätta igång BlackJack: ")
    if spela == "Starta":
        import random
        
        värde1 = random.randint(1, 11)
        print("Första kortet: " + str(värde1))
        
        värde2 = random.randint(1, 11)
        print("Andra kortet: " + str(värde2))
        
        print("Du har nu : " + str(värde1 + värde2))
        if (värde1 + värde2) > 21:
            print("DU FÖRLORADE!")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
             
            else:
                print("Hoppas vi ses snart igen!")
        if värde1 + värde2 == 21:
            print("DU FICK BLACKJACK")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
            else:
                print("Hoppas vi ses snart igen!")
                exit()
        else:
            fort_nöjd = input("Vill du få ett till kort eller är du nöjd med dina kort? Skriv 'Nöjd' eller 'Fortsätt': ")
    if fort_nöjd == "Nöjd":
        print("Okej då ska vi se vad dealern har:")
        värde6 = random.randint(1, 11)
        print("Dealerns första kort: " + str(värde6))
        
        värde7 = random.randint(1, 11)
        print("Dealerns andra kort: " + str(värde7))
        print("Dealern har: " + str(värde6 + värde7))       
        
        if (värde6 + värde7) > 21:
            print("DU VANN")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
            else:
                print("Hoppas vi ses snart igen!")
                exit()
                    
        if (värde6 + värde7) > (värde1 + värde2):
            print("DU FÖRLORADE!")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
            else:
                print("Hoppas vi ses snart igen!")
                exit()
        else:
            print("Dealern tar ett till kort")
            värde8 = random.randint(1, 11)
            print("Dealerns tredje kort:  " + str(värde8))
            
            print("Dealern har nu: " + str(värde6 + värde7 + värde8))
            if (värde6 + värde7 + värde8) > 21:
                print("DU VANN")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
        
            if (värde6 + värde7 + värde8) > (värde1 + värde2):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
            else:
                print("Dealern tar ett till kort")
                värde9 = random.randint(1, 11)
                print("Dealerns fjärde kort:  " + str(värde9))
    
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9))
                if (värde6 + värde7 + värde8 + värde9) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
            if (värde6 + värde7 + värde8 + värde9) > (värde1 + värde2):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
            else:
                print("Dealern tar ett till kort")
                värde10 = random.randint(1, 11)
                print("Dealerns femte kort:  " + str(värde10))
                
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9 + värde10))
                
                
                if (värde6 + värde7 + värde8 + värde9 + värde10) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
                
            if (värde6 + värde7 + värde8 + värde9 + värde10) > (värde1 + värde2):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
            else:
                print("Dealern tar ett till kort")
                värde11 = random.randint(1, 11)
                print("Dealerns sjätte kort:  " + str(värde11))
                
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9 + värde10 + värde11))
                if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
            if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11) > (värde1 + värde2):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
            else:
                print("Dealern tar ett till kort")
                värde12 = random.randint(1, 11)
                print("Dealerns sjunde kort:  " + str(värde12))
                
                
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9 + värde10 + värde11 + värde12))
                if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11 + värde12) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
                
                if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11 + värde12) > (värde1 + värde2):
                    print("DU FÖRLORADE!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
                    
                
                
    
    elif fort_nöjd == "Fortsätt":
        värde3 = random.randint(1, 11)
        print("Tredje kortet: " + str(värde3))
        print("Du har nu " + str(värde1 + värde2 + värde3))
        if (värde1 + värde2 + värde3) > 21:
            print("DU FÖRLORADE!")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
             
            else:
                print("Hoppas vi ses snart igen!")
                exit()
        
        fort_nöjd = input("Vill du få ett till kort eller är du nöjd med dina kort? Skriv 'Nöjd' eller 'Fortsätt': ")
    if fort_nöjd == "Nöjd":
        print("Okej då ska vi se vad dealern har:")
        värde6 = random.randint(5, 11)
        print("Dealerns första kort: " + str(värde6))
        
        värde7 = random.randint(1, 11)
        print("Dealerns andra kort: " + str(värde7))
        print("Dealern har: " + str(värde6 + värde7))
        
        if (värde6 + värde7) > 21:
            print("DU VANN")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
            else:
                print("Hoppas vi ses snart igen!")
                exit()
                    
        if (värde6 + värde7) > (värde1 + värde2 + värde3):
            print("DU FÖRLORADE!")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
            else:
                print("Hoppas vi ses snart igen!")
                exit()
        else:
            print("Dealern tar ett till kort")
            värde8 = random.randint(1, 11)
            print("Dealerns tredje kort:  " + str(värde8))
            
            print("Dealern har nu: " + str(värde6 + värde7 + värde8))
            if (värde6 + värde7 + värde8) > 21:
                print("DU VANN")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
        
            if (värde6 + värde7 + värde8) > (värde1 + värde2 + värde3):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
            else:
                print("Dealern tar ett till kort")
                värde9 = random.randint(1, 11)
                print("Dealerns fjärde kort:  " + str(värde9))
    
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9))
                if (värde6 + värde7 + värde8 + värde9) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
            if (värde6 + värde7 + värde8 + värde9) > (värde1 + värde2 + värde3):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
            else:
                print("Dealern tar ett till kort")
                värde10 = random.randint(1, 11)
                print("Dealerns femte kort:  " + str(värde10))
                
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9 + värde10))
                
                
                if (värde6 + värde7 + värde8 + värde9 + värde10) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
                
            if (värde6 + värde7 + värde8 + värde9 + värde10) > (värde1 + värde2 + värde3):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
            else:
                print("Dealern tar ett till kort")
                värde11 = random.randint(1, 11)
                print("Dealerns sjätte kort:  " + str(värde11))
                
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9 + värde10 + värde11))
                if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
            if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11) > (värde1 + värde2 + värde3):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
            else:
                print("Dealern tar ett till kort")
                värde12 = random.randint(1, 11)
                print("Dealerns sjunde kort:  " + str(värde12))
                
                
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9 + värde10 + värde11 + värde12))
                if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11 + värde12) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
                
                if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11 + värde12) > (värde1 + värde2 + värde3):
                    print("DU FÖRLORADE!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
       
       
            
        
    else: #HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
        värde4 = random.randint(1, 11)
        print("Fjärde kortet: " + str(värde4))
        print("Du har nu " + str(värde1 + värde2 + värde3 + värde4))
        if (värde1 + värde2 + värde3 + värde4) > 21:
            print("DU FÖRLORADE!")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
             
            else:
                print("Hoppas vi ses snart igen!")
         
        fort_nöjd = input("Vill du få ett till kort eller är du nöjd med dina kort? Skriv 'Nöjd' eller 'Fortsätt': ")
    if fort_nöjd == "Nöjd":
        print("Okej då ska vi se vad dealern har:")
        värde6 = random.randint(5, 11)
        print("Dealerns första kort: " + str(värde6))
        
        värde7 = random.randint(1, 11)
        print("Dealerns andra kort: " + str(värde7))
        print("Dealern har: " + str(värde6 + värde7))
        
        if (värde6 + värde7) > 21:
            print("DU VANN")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
            else:
                print("Hoppas vi ses snart igen!")
                exit()
                    
        if (värde6 + värde7) > (värde1 + värde2 + värde3 + värde4):
            print("DU FÖRLORADE!")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
            else:
                print("Hoppas vi ses snart igen!")
                exit()
        else:
            print("Dealern tar ett till kort")
            värde8 = random.randint(1, 11)
            print("Dealerns tredje kort:  " + str(värde8))
            
            print("Dealern har nu: " + str(värde6 + värde7 + värde8))
            if (värde6 + värde7 + värde8) > 21:
                print("DU VANN")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
        
            if (värde6 + värde7 + värde8) > (värde1 + värde2 + värde3 + värde4):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
            else:
                print("Dealern tar ett till kort")
                värde9 = random.randint(1, 11)
                print("Dealerns fjärde kort:  " + str(värde9))
    
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9))
                if (värde6 + värde7 + värde8 + värde9) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
            if (värde6 + värde7 + värde8 + värde9) > (värde1 + värde2 + värde3 + värde4):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
            else:
                print("Dealern tar ett till kort")
                värde10 = random.randint(1, 11)
                print("Dealerns femte kort:  " + str(värde10))
                
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9 + värde10))
                
                
                if (värde6 + värde7 + värde8 + värde9 + värde10) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
                
            if (värde6 + värde7 + värde8 + värde9 + värde10) > (värde1 + värde2 + värde3 + värde4):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
            else:
                print("Dealern tar ett till kort")
                värde11 = random.randint(1, 11)
                print("Dealerns sjätte kort:  " + str(värde11))
                
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9 + värde10 + värde11))
                if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
            if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11) > (värde1 + värde2 + värde3 + värde4):
                print("DU FÖRLORADE!")
                förlust = input("Vill du spela igen? Ja eller Nej: ")
                if förlust == "Ja":
                    main()
                else:
                    print("Hoppas vi ses snart igen!")
                    exit()
            else:
                print("Dealern tar ett till kort")
                värde12 = random.randint(1, 11)
                print("Dealerns sjunde kort:  " + str(värde12))
                
                
                print("Dealern har nu: " + str(värde6 + värde7 + värde8 + värde9 + värde10 + värde11 + värde12))
                if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11 + värde12) > 21:
                    print("DU VANN!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
                
                if (värde6 + värde7 + värde8 + värde9 + värde10 + värde11 + värde12) > (värde1 + värde2 + värde3 + värde4):
                    print("DU FÖRLORADE!")
                    förlust = input("Vill du spela igen? Ja eller Nej: ")
                    if förlust == "Ja":
                        main()
                    else:
                        print("Hoppas vi ses snart igen!")
                        exit()
                        
    else:
        värde5 = random.randint(1, 11)
        print("Femte kortet: " + str(värde5))
        print("Du har nu " + str(värde1 + värde2 + värde3 + värde4 + värde5))
        if (värde1 + värde2 + värde3 + värde4 + värde5) <= 21:
            print("DU VANN!")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
            else:
                print("Hoppas vi ses snart igen!")
        else:
            print("DU FÖRLORADE!")
            förlust = input("Vill du spela igen? Ja eller Nej: ")
            if förlust == "Ja":
                main()
            else:
                print("Hoppas vi ses snart igen!")
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            
            
            
            
            
                
            
                
                
                
                
                
                
                
                
                
            
                    
                                
                
                
    



























main()
   
















        
        
