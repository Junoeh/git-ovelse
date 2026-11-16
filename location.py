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
        win()
    else:
        print("Ugyldig valg!")
        corridor()


def police():
    print("\nDu gikk inn i et rom fullt av politi.")
    print("Du tapte!")


def win():
    print("Du klarte å rømme fra fengselet!")
    print("Du vant!")


# Starter spillet
def start():
    cell()
