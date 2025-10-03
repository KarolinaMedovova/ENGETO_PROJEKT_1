ukoly = []

def hlavni_menu():
    print(" ")
    print("Správce úkolů - Hlavní menu\n1. Přidat nový úkol\n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu")


def pridat_ukol():
    print(" ")
    nazev_ukolu = input("Zadejte název úkolu: ")
    while nazev_ukolu.isspace() or nazev_ukolu == "":
        print("Byl zadán prázdný vstup. Zadejte název úkolu.")
        print(" ")
        nazev_ukolu = input("Zadejte název úkolu: ")
        
    popis_ukolu = input("Zadejte popis úkolu: ")
    while popis_ukolu.isspace() or popis_ukolu == "":
        print("Byl zadán prázdný vstup. Zadejte popis úkolu.")
        print(" ")
        popis_ukolu = input("Zadejte popis úkolu: ")

    print(f"Úkol '{nazev_ukolu}' byl přidán.")
    ukoly.append(f"{nazev_ukolu} - {popis_ukolu}")


def zobrazit_ukoly():
    print(" ")
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return
    
    print("Seznam úkolů:")
    for index, ukol in enumerate(ukoly, start=1):
        print(f"{index}. {ukol}")


def odstranit_ukol():#
    if not ukoly:
        print(" ")
        print("Seznam úkolů je prázdný, žádný úkol nelze odstranit. Prosím, zadejte možnost 1 nebo 4.")
        return
    print(" ")
    print("Seznam úkolů:")
    for index, work in enumerate(ukoly, start=1): 
        ocislovane_ukoly = (f"{index}. {work}")
        print(ocislovane_ukoly)
    print(" ")

    task_number = input("Zadejte číslo úkolu, který chcete odstranit. (Pro návrat do hlavního menu zadejte 'x'.): ")
    if task_number == "x":
        return
    elif not task_number.isdigit() or int(task_number) < 1 or int(task_number) > len(ukoly):
        print("Bylo zadáno neexistující číslo úkolu.")
        task_number = input("Zadejte číslo úkolu, který chcete odstranit: ")
    
    task_index = int(task_number) -1
    odstraneny = ukoly.pop(task_index)
    nazev = odstraneny.split(" - ")[0]
    print(f"Úkol '{nazev}' byl odstraněn.")


def konec_programu():
    print(" ")
    print("Konec programu.")


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
        print(" ")
        print("Byla zadána neplatná volba. Prosím, zvolte možnost 1, 2, 3 nebo 4.")