ukoly = []
ocislovany_seznam_ukolu = []    #musí být jiný náazev. ocislovane_ukoly je proměnná, stejný mázev nemůžu mít pro seznam !!!
nazvy_ukolu = []
popisy_ukolu = []

def hlavni_menu():
    print("Správce úkolů - Hlavní menu\n1. Přidat nový úkol\n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu")
    
hlavni_menu()

def ocislovat_ukoly():
    for index, ukol in enumerate(ukoly, start=1):
        print(f"{index}. {ukol}")
    print(" ")
    ocislovane_ukoly = (f"{index}. {ukol}")
    ocislovany_seznam_ukolu.append(ocislovane_ukoly)

def pridat_ukol():
    print(" ")
    nazev_ukolu = input("Zadejte název úkolu: ")
    while nazev_ukolu.isspace() or nazev_ukolu == "":   #nebo nazev_ukolu == "", len(nazev_ukolu) == 0
        print("Byl zadán prázdný vstup. Zadejte název úkolu.")
        print(" ")
        nazev_ukolu = input("Zadejte název úkolu: ")
        
    popis_ukolu = input("Zadejte popis úkolu: ")
    while popis_ukolu.isspace() or popis_ukolu == "":   #nebo popis_ukolu == "", len(popis_ukolu) == 0
        print("Byl zadán prázdný vstup. Zadejte popis úkolu.")
        print(" ")
        popis_ukolu = input("Zadejte popis úkolu: ")

    print(f"Úkol '{nazev_ukolu}' byl přidán.")
    print(" ")
    hlavni_menu()
    ukoly.append(f"{nazev_ukolu} - {popis_ukolu}")
"""   
    nazvy_ukolu.append(nazev_ukolu)
    popisy_ukolu.append(popis_ukolu)
    
    for index, ukol in enumerate(ukoly, start=1):
        ocislovane_ukoly = (f"{index}. {ukol}")
        ocislovany_seznam_ukolu.append(ocislovane_ukoly)
"""

def zobrazit_ukoly():
    print(" ")
    print("Seznam úkolů:")
    for index, ukol in enumerate(ukoly, start=1):
        print(f"{index}. {ukol}")
    print(" ")
    hlavni_menu()

def odstranit_ukol():
    print(" ")
    print("Seznam úkolů:")
    for index, work in enumerate(ukoly, start=1):
        ocislovane_ukoly = (f"{index}. {work}")
        print(ocislovane_ukoly)
    ocislovany_seznam_ukolu.append(ocislovane_ukoly)
    print(" ")
    task_number = int(input("Zadejte číslo úkolu, který chcete odstranit: "))

    while type(task_number) is not int or task_number <1: #or task_number == "" or task_number.isspace():
        print("Bylo zadáno neexistující číslo úkolu.")
        task_number = int(input("Zadejte číslo úkolu, který chcete odstranit: "))

    task_index = int(task_number) -1
    odstraneny = ukoly.pop(task_index)
    nazev = odstraneny.split(" – ")[0]

    print(f"Úkol '{nazev}' byl odstraněn.")
    print(" ")
    print("Správce úkolů - Hlavní menu\n1. Přidat nový úkol\n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu")

def konec_programu():
    print(" ")
    print("Konec programu.")


while True:
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
        print("Byla zadána neplatná volba. Prosím, zvolte možnost 1, 2, 3 nebo 4.")
