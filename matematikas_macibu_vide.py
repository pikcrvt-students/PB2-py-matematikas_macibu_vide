"""Programma, kas palīdz matemātikas skolotājai, atvieglojot viņas darbu.
Programma dod iespēju izvēlēties teoriju, pildīt patstāvīgos uzdevumus vai pildīt pārbaudes darbu

Izveidoja: Kristiāns Kokars
V0.0
"""


def atzime(rezultats, maksimali):
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


temas = ['1. Kvadrātvienādojums']  # tēmu saraksts


def teorija():
    print('Izvēlies teoriju:', *temas, sep='\n')
    teorijaNr = int(input('Izvēle: '))  # dod iespēju izvēlēties par kuru tēmu lasīt teoriju
    print()
    if teorijaNr == 1:  # izvada izvēlēto teoriju
        print('Teorija:\n', temas[0], '''\n
    Vienādojumu ax2+bx+c=0, kur a, b un c - reāli skaitļi, a≠0, sauc par kvadrātvienādojumu.
    Piemērs:
     4x^2−3x+1=0
     a=4
     b=−3
     c=1
    Kvadrātvienādojuma saknes var atrast pēc formulām:
    x1=(−b+√D)/2ax
    2=(−b−√D(/2a,
    kur D=b^2−4ac.
     
    D sauc par diskriminantu.
    Pēc diskriminanta vērtības var noteikt kvadrātvienādojuma sakņu skaitu.
     Ja D<0 (negatīvs), tad vienādojumam nav atrisinājuma reālo skaitļu kopā
    Ja D=0, tad vienādojumam ir divas vienādas saknes
    Ja D>0 (pozitīvs), tad vienādojumam ir divas dažādas saknes.
    Kvadrātvienādojumu x^2+bx+c=0 var risināt arī pēc Vjeta teorēmas:
    {x1⋅x2=c  x1+x2=−b 
    Ievēro: koeficients pie x^2 ir a=1!
    (Atrisināšanas piemērus skat. pie uzdevumiem.)
    
    Nepilnie kvadrātvienādojumi
    
    Ir divu veidu nepilnie kvadrātvienādojumi:
    Ja c=0, tad vienādojums ir ax^2+bx=0;
    Ja b=0, tad ax^2+c=0.
      
    Nepilnos kvadrātvienādojumus drīkst risināt ar diskriminanta formulām,
    bet racionālāk būs izvēlēties speciālas metodes:
     
    1) ax^2+bx=0 risina, sadalot reizinātājos (iznesot pirms iekavām x).
     
    x(ax+b)=0
    Tātad x=0 vai ax+b=0. (Jo divu skaitļu reizinājums ir nulle tad un tikai tad,
    ja vismaz viens no šiem skaitļiem ir 0.)
    Viena sakne ir 0, bet otra sakne ir x=−b/a.
    Piemērs:
    2x^2−30x=0
    x(2x−30)=0
    1)x=0
    2)2x−30=0⇔2x=30⇔x=15
     
    Atbilde: x1=0, x2=15.
    2) ax^2+c=0 risina, pārnesot saskaitāmos dažādās pusēs un tad velkot kvadrātsakni.
    
    ax^2=−c (izdala abas puses ar a)
    x^2=−c/a
    |x|=√(−c/a)
    (Ievēro: velkot sakni, iegūst x moduļa vērtību!)
     
    Tas nozīmē, ka
    x1=√(−c/a)
    x2=-√(−c/a)
    Piemērs:
    4x^2−100=0
    4x^2=100 ∣:4
    x^2=25
    |x|=√25
    x1=5; x2=5
     
    Atbilde: x1=5; x2=−5.
    Piemērs:
    x^2+36=0
    x^2=−36
    Šim vienādojumam nav atrisinājuma, jo kvadrātsakni nedrīkst vilkt no negatīva skaitļa 
    (zinām arī, ka skaitli kāpinot kvadrātā, nevar iegūt negatīvu skaitli).
     
    Atbilde: sakņu nav.''')


def patstavigais_darbs():
    global punkti, atb_sk
    punkti = 0
    atb_sk = 0
    print('Izvēlies tēmu priekš patstāvīgā darba:', *temas, sep='\n')
    temaNr = int(input('Izvēle: '))  # dod iespēju izvēlēties par kuru tēmu pildīt patstāvīgo darbu
    print()
    if temaNr == 1:
        jautajumi = [['Atrisini nepilno kvadrātvienādojumu:\n4x^2−36x=0\n\nPirmo ievadi mazāko sakni', 0, 9],
                     ['Kādas ir nepilnā kvadrātvienādojuma:\n2x^2−18=0 saknes?\n\nVispirms ievadi lielāko sakni!', 3, -3],
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
    atzime(punkti, atb_sk)


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
                    print('Kļūda!')
                    print('Pareizā atbilde:', jautajumi[i][atb], 'Nevis', atbilde)
    else:
        print('Tādas tēmas numura nav!\n')
        patstavigais_darbs()
    atzime(punkti, atb_sk)


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


lietotaja_izveles()
