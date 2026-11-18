def cell():
    print("Du er i en fengselscelle.")
    print("1. Ødelegg veggen")
    print("2. Ødelegg døra")

    choice = input("Velg: ")

    if choice == "1":
        wall()
    elif choice == "2":
        corridor()
    else:
        print("Ugyldig valg!")
        cell()


def wall():
    print("Du kom til en annen fengselscelle.")
    print("Du tapte!")


def corridor():
    print("Du er i gangen.")
    print("1. Gå gjennom døra på høyre side")
    print("2. Gå gjennom døra på venstre side")

    choice = input("Velg: ")

    if choice == "1":
        police()
    elif choice == "2":
        prisonyard()
    else:
        print("Ugyldig valg!")
        corridor()

def prisonyard():
    print("Du er i fengselsgården.")
    print("1. Snakk med mannen ved hjørnet")
    print("2. Hopp over gjerdet")
    choice = input("Velg: ")
    
    if choice == "1":
            crazyman()
    elif choice == "2":
            win()
    else:
            print("Ugyldig valg!")
            corridor()



def crazyman():
    print("Mannen skriker")
    print("Politiet kommer løpene ut")
    print("Du tapte!")

def police():
    print("Du gikk inn i et rom fullt av politi.")
    print("Du tapte!")


def win():
    print("Du klarte å rømme fra fengselet!")
    print("Du vant!")


# Starter spillet
def start():
    cell()
