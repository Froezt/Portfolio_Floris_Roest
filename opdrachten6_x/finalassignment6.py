def toon_aantal_kluizen_vrij():
    num_lines = sum(1 for line in open('kluizen.txt'))
    kluizenvrij = 12 - num_lines
    print('Er zijn ' + str(kluizenvrij) + ' kluizen vrij.')
    return

def nieuwe_kluis():
    return

def kluis_openen():
    kluisnummer = eval(input('Voer uw kluisnummer in: '))
    wachtwoord = str(input('Voer uw wachtwoord in: '))
    f = open('kluizen.txt', 'r')
    koek = f.readline()
    return

def kluis_teruggeven():
    kluisnummer = eval(input('Voer uw kluisnummer in: '))
    wachtwoord = str(input('Voer uw wachtwoord in: '))
    return

print("1: Ik wil weten hoeveel kluizen nog vrij zijn.\n2: Ik wil een nieuwe kluis. \n3: Ik wil even iets uit mijn kluis halen. \n4: Ik geef mijn kluis terug")
optie = eval(input('Kies een optie: '))

if optie == int('1'):
    toon_aantal_kluizen_vrij()
elif optie == int('2'):
    print('koek in de hoek')
elif optie == int('3'):
    kluis_openen()
elif optie == int('4'):
    kluis_teruggeven()