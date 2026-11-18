from imgcat import imgcat


class Handling:
    def __init__(self, verdi):
        self.verdi = verdi


class ByttRom(Handling):
    def utfor(self, spill):
        spill.rom = self.verdi


class EndreBilde(Handling):
    def utfor(self, spill):
        spill.rom.bilde = self.verdi


class Valg:
    def __init__(self, tekst, handling):
        self.tekst = tekst
        self.handling = handling


class Rom:
    def __init__(self, tekst, bilde):
        self.tekst = tekst
        self.bilde = bilde
        self.valg = []

    def vis(self):
        print(self.tekst)
        print("Bilde:", self.bilde)

        for valg in self.valg:
            print(valg.tekst)


class Spill:
    def __init__(self, rom):
        self.rom = rom

    def start(self):
        print("PRISON ESCAPEw")

        while True:
            self.rom.vis()

            if self.rom.valg == []:
                break

            svar = input("Velg: ")

            if svar == "1":
                valg = self.rom.valg[0]
                handling = valg.handling
                handling.utfor(self)

            elif svar == "2":
                valg = self.rom.valg[1]
                handling = valg.handling
                handling.utfor(self)

            else:
                print("Ugyldig valg")


celle = Rom("Du er i en fengsels.", "celle.png")
gang = Rom("Du er i gangen.", "gang.png")
vegg = Rom("Du kom til en annen fengselscelle. Du tapte!", "vegg.png")
politi = Rom("Du ble tatt av politiet. Du tapte!", "politi.png")
fri = Rom("Du klarte DET Du vant!", "free.png")


celle.valg = [
    Valg("1. Ødelegg veggen", ByttRom(vegg)),
    Valg("2. Ødelegg døra", ByttRom(gang))
]


gang.valg = [
    Valg("1. Gå til høyre", ByttRom(politi)),
    Valg("2. Gå til venstre", ByttRom(fri))
]


spill = Spill(celle)
spill.start()
