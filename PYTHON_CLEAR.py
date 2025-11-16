ukoly = []
ukoly_DB = []


#Definuji funkci hlavního menu
def hlavni_menu():
    print("" "\nSprávce úkolů - Hlavní menu\n1. Přidat nový úkol\n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu")


#Definuji funkci pro přidání úkolu
def pridat_ukol():
    print(" ")
    nazev_ukolu = input("Zadejte název úkolu: ")
    #když je název prázný nebo uživatel zadá omylem Enter:
    while nazev_ukolu.isspace() or nazev_ukolu == "":
        print("Byl zadán prázdný vstup. Zadejte název úkolu.\n" "")
        nazev_ukolu = input("Zadejte název úkolu: ")
        
    popis_ukolu = input("Zadejte popis úkolu: ")
    #když je název prázný nebo uživatel zadá omylem Enter:
    while popis_ukolu.isspace() or popis_ukolu == "":
        print("Byl zadán prázdný vstup. Zadejte popis úkolu.\n" "")
        popis_ukolu = input("Zadejte popis úkolu: ")

    print(f"Úkol '{nazev_ukolu}' byl přidán.")
    
    novy_ukol = {
    "nazev" : nazev_ukolu, 
    "popis" : popis_ukolu
    }

    global ukoly_DB
    #Přidaný úkol se uloží do seznamu úkolů:
    ukoly_DB.append(novy_ukol)
    ukoly.append(f"{nazev_ukolu} - {popis_ukolu}")


#Definuji funkci pro zobrazení očíslovaného seznamu úkolů
def tasks_list():
    print("Seznam úkolů:")
    for index, ukol in enumerate(ukoly_DB, start=1):
        print(f"{index}. {ukol["nazev"]} - {ukol["popis"]}")


#Definuji funkci pro zobrazení seznamu úkolů
def zobrazit_ukoly():
    print(" ")
    if not ukoly_DB:
        print("Seznam úkolů je prázdný. Prosím, zadejte možnost 1 nebo 4.")
        return
    
    tasks_list()


#Definuji funkci pro odstranění úkolu
def odstranit_ukol():
    global ukoly_DB
    #když je seznam prázdný:
    if not ukoly_DB:
        print("" "\nSeznam úkolů je prázdný, žádný úkol nelze odstranit. Prosím, zadejte možnost 1 nebo 4.")
        return
    print(" ")
    tasks_list()
    print(" ")

    while True:
        task_number = input("Zadejte číslo úkolu, který chcete odstranit. (Pro návrat do hlavního menu zadejte 'x'.): ")
        if task_number.lower() == "x":
            return
        elif task_number.isdigit() and int(task_number) >= 1 and int(task_number) <= len(ukoly_DB):
            task_index = int(task_number) -1
            odstraneny = ukoly_DB.pop(task_index)
            print(f"Úkol '{odstraneny["nazev"]}' byl odstraněn.")
            return
        else:
            print("Bylo zadáno neexistující číslo úkolu.\n" "")
   
   
#Definuji funkci pro ukončení programu
def konec_programu():
    print("" "\nKonec programu.")
    

while True:
    hlavni_menu()
    option = input("Vyberte možnost (1-4): ")
    if option == "1":
        pridat_ukol()  
    elif option == "2":
        zobrazit_ukoly()
    elif option == "3":
        odstranit_ukol()
    elif option == "4":
        konec_programu()
        break
    else:
        print("" "\nByla zadána neplatná volba. Prosím, zvolte možnost 1, 2, 3 nebo 4.")
