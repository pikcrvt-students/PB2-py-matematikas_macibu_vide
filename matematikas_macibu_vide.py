"""Programma, kas palīdz matemātikas skolotājai, atvieglojot viņas darbu.
Programma dod iespēju izvēlēties teoriju, pildīt patstāvīgos uzdevumus vai pildīt pārbaudes darbu

Izveidoja: Kristiāns Kokars
V0.1
"""


def atzime(rezultats, maksimali, darbs):
    print()
    vertejums = rezultats / maksimali  # aprēķina rezultātu 0-1
    if vertejums <= 0.1:  # nosaka kāds ir vērtējums
        print('Vērtējums: 1(ļoti, ļoti vāji)')
    elif vertejums <= 0.2:
        print('Vērtējums: 2(ļoti vāji)')
    elif vertejums <= 0.3:
        print('Vērtējums: 3(vāji)')
    elif vertejums <= 0.4:
        print('Vērtējums: 4(gandrīz viduvēji)')
    elif vertejums <= 0.5:
        print('Vērtējums: 5(viduvēji)')
    elif vertejums <= 0.6:
        print('Vērtējums: 6(gandrīz labi)')
    elif vertejums <= 0.7:
        print('Vērtējums: 7(labi)')
    elif vertejums <= 0.8:
        print('Vērtējums: 8(ļoti labi)')
    elif vertejums <= 0.9:
        print('Vērtējums: 9(teicami)')
    elif vertejums <= 1:
        print('Vērtējums: 10(izcili)')
    if darbs == 'kontr':
        lietotajs.append(vertejums*10)
        atzimes_saglab()


def atzimes_saglab():
    atzimes_f = open('atzimes.txt', 'a', encoding='utf8')
    atzimes_f.write(f'{lietotajs}\n')
    atzimes_f.close()


def teorija():
    teoriju_f = open('teorija.txt', 'r', encoding='utf8')
    teorijas = teoriju_f.read()
    teoriju_f.close()
    print('Izvēlies teoriju:', *temas, sep='\n')
    while True:
        teorijaNr = int(input('Izvēle: '))  # dod iespēju izvēlēties par kuru tēmu lasīt teoriju
        print()
        if teorijaNr == 1:  # izvada izvēlēto teoriju
            print('Teorija:\n ', temas[0], '\n', teorijas, sep='')
            break
        else:
            print('Nepareiza ievade!\n')


def patstavigais_darbs():
    global punkti, atb_sk
    punkti = 0
    atb_sk = 0
    print('Izvēlies tēmu priekš patstāvīgā darba:', *temas, sep='\n')
    temaNr = int(input('Izvēle: '))  # dod iespēju izvēlēties par kuru tēmu pildīt patstāvīgo darbu
    print()
    if temaNr == 1:
        jautajumi = [['Atrisini nepilno kvadrātvienādojumu:\n4x^2−36x=0\n\nPirmo ievadi mazāko sakni', 0, 9],
                     ['Kādas ir nepilnā kvadrātvienādojuma:\n2x^2−18=0 saknes?\n\nVispirms ievadi lielāko sakni?', 3, -3],
                     ['Aprēķini kvadrātvienādojuma:\nx^2+7x+12=0 saknes?\n\nJa abas saknes nav vienādas, tad pirmo ievadi lielāko sakni!', -3, -4]
                     ]
        for i in range(len(jautajumi)):
            print(jautajumi[i][0])
            uzdevuma_gar = len(jautajumi[i])
            for atb in range(1, uzdevuma_gar):
                atbilde = float(input())
                atb_sk += 1
                if atbilde == jautajumi[i][atb]:
                    punkti += 1
                else:
                    print('Kļūda!')
                    print('Pareizā atbilde:', jautajumi[i][atb], 'Nevis', atbilde)
    else:
        print('Tādas tēmas numura nav!\n')
        patstavigais_darbs()
    atzime(punkti, atb_sk, "patst")


def kontroldarbs():
    global punkti, atb_sk
    punkti = 0
    atb_sk = 0
    print('Izvēlies tēmu priekš pārbaudes darba:', *temas, sep='\n')
    temaNr = int(input('Izvēle: '))  # dod iespēju izvēlēties par kuru tēmu pildīt patstāvīgo darbu
    print()
    if temaNr == 1:
        jautajumi = [['Nosaki saknes nepilnajam kvadrātvienādojumam:\n4x^2−8x=0\n\nPirmo ievadi mazāko sakni', 0, 2],
                     ['Kādas ir nepilnā kvadrātvienādojuma 2x^2−8=0 saknes?\n\nVispirms ievadi lielāko sakni!', 2, -2],
                     ['Atrisini kvadrātvienādojumu x^2−7x+12=0!\n\nPirmo ievadi lielāko sakni', 4, 3],
                     ['Atrisini kvadrātvienādojumu 2x^2−6x+4=0!\n\nPirmo ievadi lielāko sakni!', 2, 1]
                     ]
        for i in range(len(jautajumi)):
            print(jautajumi[i][0])
            uzdevuma_gar = len(jautajumi[i])
            for atb in range(1, uzdevuma_gar):
                atbilde = float(input())
                atb_sk += 1
                if atbilde == jautajumi[i][atb]:
                    punkti += 1
    else:
        print('Tādas tēmas numura nav!\n')
        patstavigais_darbs()
    atzime(punkti, atb_sk, "kontr")


def lietotaja_izveles():
    izvele = input('Darbību izvēle:\n1. Atvērt teoriju\n2. Pildīt patstāvīgo darbu\n3. Pildīt pārbaudes darbu\nIzvēle:')
    if izvele == '1':
        print()
        teorija()
    elif izvele == '2':
        print()
        patstavigais_darbs()
    elif izvele == '3':
        print()
        kontroldarbs()
    else:
        print('Nepareiza ievade!')
        lietotaja_izveles()


def lietotaja_saglabasana():
    global lietotajs
    vards = input('Kāds ir tavs vārds: ')
    uzvards = input('Kāds ir tavs uzvārds: ')
    lietotajs = [vards, uzvards]


temas = ['1. Kvadrātvienādojums']  # tēmu saraksts

"""
cilki, kas ļauj lietotājam izvēlēties vai sākt un beigt darbus, 
kad lietotājs beidzis tiek dota izvele nākošajam lietotājam.

"""
while True:
    start = input('Vai tu vēlies sākt darbu?\n1. Jā\n2. Nē\nIzvēle: ')
    if start == '1':
        lietotaja_saglabasana()
        while True:
            lietotaja_izveles()
            izvele = input('Vai tu vēlies atgriesties izvēlnē?\n1. Jā\n2. Nē\nIzvēle: ')
            print()
            if izvele == '2':
                print('Visu labu!\n\nNākamais lietotājs:')
                break
    else:
        print('Beigas')
        break