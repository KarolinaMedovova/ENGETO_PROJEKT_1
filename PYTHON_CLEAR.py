# 21.7.2025
ukoly = []

def hlavni_menu():
    print("Správce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")
    
hlavni_menu()

def user_input():
    moznost=int(input("Vyberte možnost (1-4) : "))


def pridat_ukol():
    nazev_ukolu = input("Zadejte název úkolu: ")
    while nazev_ukolu.isspace() or nazev_ukolu == "":   #nebo nazev_ukolu == "", len(nazev_ukolu) == 0
        print("Byl zadán prázdný vstup. Zadej název úkolu.")
        nazev_ukolu = input("Zadejte název úkolu: ")
    popis_ukolu = input("Zadejte popis úkolu: ")
    while popis_ukolu.isspace() or popis_ukolu == "":   #nebo popis_ukolu == "", len(popis_ukolu) == 0
        print("Byl zadán prázdný vstup. Zadej popis úkolu.")
        popis_ukolu = input("Zadejte popis úkolu: ")
    ukoly.append(f"{nazev_ukolu} - {popis_ukolu}")

    print("Úkol "+"'"+nazev_ukolu+"'"+" byl přidán.")
    print(" ")
    hlavni_menu()


def zobrazit_ukoly():
    print(f"{ukoly}")
    print(" ")
    hlavni_menu()

while True:
    moznost=input("Vyberte možnost (1-4) : ")
    if moznost == "1":
        #print("1. Přidat nový úkol")
        pridat_ukol()  
             
    elif moznost == "2":
        print("Seznam úkolů: ")
        zobrazit_ukoly()

    elif moznost == "3":
        #print("3. Odstranit úkol")
        odstranit_ukol()

    elif moznost == "4":
        print(" ")
        print("Konec programu")
        exit()
    else:
        print("Byla zadána neplatná volba. Prosím, zvolte možnost 1, 2, 3 nebo 4.")