#Powitanie
#Alfabet Morsea
print('Witaj w symulatorze nauki alfabetu Morsea!')
print('Jeśli chcesz nauczysz się wielu przydatnych zwrotów :)')
#pytanie o chęć
print('Jeśli jesteś gotowy odpowiedz Tak, jeśli nie to Nie.')
answear = input('Czy jesteś gotowy: ')
if answear == 'Tak':
    #Zapytaj o imię
    name = input('Jak masz na imię?: ')
    print("Nauka jest podzielona na wiele etapów, jeśli znasz jakiś napisz 'Znam ten etap', jeśli nie po prostu kliknij enter.")
    #ALFABET
    LEVEL1 = input('Zaczniemy od alfabetu.')
    if LEVEL1 != 'Znam ten etap':
        print("Jeśli znasz daną literę napisz 'Znam tą literę', wtedy ją pominę")
        print('Jeśli nie znasz danej litery kliknij ENTER')
        print('No to zaczynajmy', name, '!')
        yes1 = input('Teraz litera A')
        if yes1 == 'Znam tą literę':
            print('Okay')
        else:
            print('Litera A to .-')
        A = input('Napisz literę A: ')
        while A != '.-':
            A = input('Jeszcze raz: ')
        print('Bardzo dobrze')
        yes2 = input('Teraz litera B')
        if yes2 == 'Znam tą literę':
            print('Okay')
        else:
            print('Litera B to -...')
        B = input('Napisz literę B: ')
        while B != '-...':
            B = input('Jeszcze raz: ')
        print('Bardzo dobrze!')
        yes3 = input('Teraz litera C')
        if yes3 == 'Znam tą literę':
            print('Okay')
        else:
            print('Litera C to -.-.')
        C = input('Napisz literę C: ')
        while C != '-.-.':
            C = input('Napisz jeszcze raz: ')
        print('Dobrze Ci idzie!')
        yes4 = input('Teraz litera D')
        if yes4 == 'Znam tą literę':
            print('Okay')
        else:
            print('Litera D to -..')
        D = input('Napisz literę D: ')
        while D != '-..':
            D = input('Jeszcze raz: ')
        print('Bardzo dobrze')
        yes5 = input('Teraz litera E')
        while yes5 == 'Znam tą literę':
            print('Okay')
        else:
            print('Litera E to .')
        E = input('Napisz literę E: ')
        while E != '.':
            E = input('Spróbuj jeszcze raz: ')
        print('Świetnie Ci idze:)')
        yes6 = input('Teraz litera F')
        if yes6 == 'Znam tą literę':
            print('Okay')
        else:
            print('Litera F to ..-.')
        F = input('Napisz literę F: ')
        while F != '..-.':
            F = input('Napisz jeszcze raz literę F: ')
        print('Świetnie Ci idzie')
        yes7 = input('Teraz litera G')
        if yes7 == 'Znam tą literę':
            print('Okay')
        else:
            print('Litera G to --.')
        G = input('Napisz literę G: ')
        while G != '--.':
            G = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Bardzo dobrze')
        yes8 = input('Teraz litera H')
        if yes8 == 'Znam tą literę':
            print('No dobra')
        else:
            print('Litera H to ....')
        H = input('Napisz literę H: ')
        while H != '.....':
            H = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Bardzo dobrze!')
        yes9 = input('Teraz litera I')
        if yes9 == 'Znam tą literę':
            print('Okay')
        else:
            print('Litera I to ..')
        I = input('Napisz literę I: ')
        while I != '..':
            I = input('Nie tym razem, spróbuj jeszcze raz: ')
        print('Naprawdę dobrze')
        yes10 = input('Teraz litera J')
        if yes10 == 'Znam tą literę':
            print('No to pomijamy')
        else:
            print('Litera J to .---')
        J = input('Napisz literę J: ')
        if J != '.---':
            J = input('Spróbuj jeszcze raz: ')
        print('Naprawdę bardzo dobrze')
        yes11 = input('Teraz litera K')
        if yes11 == 'Znam tą literę':
            print('Okay', name)
        else:
            print('Litera K to -.-')
        K = input('Napisz literę K: ')
        while K != '-.-':
            K = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Świetnie')
        yes12 = input('Teraz litera L')
        if yes12 == 'Znam tą literę':
            print('Oooookay')
        else:
            print('Liters L to .-..')
        L = input('Napisz literę L: ')
        while L != '.-..':
            L = input('Błąd! Spróbuj jeszcze raz')
        print('Świetnie!')
        yes13 = input('Teraz czas na literę M')
        if yes13 == 'Znam tą literę':
            print('To pomijam')
        else:
            print('Litera M to --')
        M = input('Napisz literę M: ')
        while M != '--':
            M = input('Nie tym razem, spróbuj jeszcze raz')
        print('Bardzo dobrze!')
        yes14 = input('Teraz litera N')
        if yes14 == 'Znam tą literę':
            print('No skoro tak')
        else:
            print('Litera N to -.')
        N = input('Napisz literę N: ')
        while N != '-.':
            N = input('Spróbuj raz jeszcze')
        print('Coraz więcej umiesz.')
        yes15 = input('Teraz litera O')
        if yes15 == 'Znam tą literę':
            print('Okay, to pomijam.')
        else:
            print('Litera O to ---')
        O = input('Napisz literę O: ')
        while O != '---':
            O = input('Niestety, nie zgadza się, spróbuj jeszcze raz: ')
        print('Bardzo dobrze.')
        yes16 = input('Czas na literę P')
        if yes16 == 'Znam tą literę':
            print('No zaraz się okaże ;)')
        else:
            print('Litera P to .--.')
        P = input('Napisz literę P: ')
        while P != '.--.':
            P = input('Nie tym razem, spróbuj jeszcze raz: ')
        print('Bardzo dobrze:)')
        yes17 = input('Czas na literę Q')
        if yes17 == 'Znam tą literę':
            print('Okay.')
        else:
            print('Litera Q to --.-')
        Q = input('Napisz literę Q: ')
        while Q != '--.-':
            Q = input('Nie tym razem, spróbuj jeszcze raz: ')
        print('Świetnie Ci idzie.')
        yes18 = input('Teraz litera R')
        if yes18 == 'Znam tą literę':
            print('To pomijam.')
        else:
            print('Litera R to .-.')
        R = input('Napisz literę R: ')
        while R != '.-.':
            R = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Bardzo dobrze.')
        yes19 = input('Teraz czas na literę S.')
        if yes19 == 'Znam tą literę':
            print('Okay.')
        else:
            print('Litera S to ...')
        S = input('Napisz literę S: ')
        while S != '...':
            S = input('Nie tym razem, spróbuj jeszcze raz: ')
        print('Naprawdę świetnie Ci idzie!')
        yes20 = input('Czas na literę T.')
        if yes20 == 'Znam tą literę':
            print('No skoro tak, to pomijam.')
        else:
            print('Litera T to -')
        T = input('Napisz literę T: ')
        while T != '-':
            T = input('Błąd! Spróbuj jeszcze raz: ')
        print('Świetnie', name)
        yes21 = input('Już czas na U.')
        if yes21 == 'Znam tą literę':
            print('Niech Ci bedzie', name)
        else:
            print('Litera U to ..-')
        U = input('Napisz literę U: ')
        while U != '..-':
            U = input('Nie tym razem, spróbuj jeszcze raz: ')
        print('No no, lecimy dalej.')
        yes22 = input('Czas to pieniądz więc lecimy dalej, czas na V.')
        if yes22 == 'Znam tą literę':
            print('Nooo to pomijam.')
        else:
            print('V to ...-')
        V = input('Napisz literę V: ')
        while V != '...-':
            V = input('No niestety bład, spróbuj jeszcze raz: ')
        print('Już prawie koniec.')
        yes23 = input('Kolejnej litery czas, tym razem to W.')
        if yes23 == 'Znam tą literę':
            print('Skoro tak.')
        else:
            print('Litera W to .--')
        W = input('Napisz literę W: ')
        while W != '.--':
            W = input('Tak mi przykro, spróbuj jeszcze raz: ')
        print('No no, jako program jestem dumny.')
        yes24 = input('Teraz czas na X.')
        if yes24 == 'Znam tą literę':
            print('Więc pomijam.')
        else:
            print('Litera X to -..-')
        X = input('Napisz literę X: ')
        while X != '-..-':
            X = input('No nie, spróbuj jeszcze raz: ')
        print('Coraz bliżej końca ;)')
        yes25 = input('Pora na Y.')
        if yes25 == 'Znam tą literę':
            print('Skoro tak.')
        else:
            print('Litera Y to -.--')
        Y = input('Napisz Y: ')
        while Y != '-.--':
            Y = input('Uczymy się na błędach, spróbuj jeszcze raz: ')
        print('Pora na ostatnią literę.')
        yes26 = input('Ostatnia litera w alfabecie morsea to Z, czas na nią.')
        if yes26 == 'Znam tą literę':
            print('No no.')
        else:
            print('Z to --..')
        Z = input('Napisz literę Z: ')
        while Z != '--..':
            Z = input('Prawie ale nie, spróbuj jeszcze raz: ')
        print('No to mamy już cały alfabet, BRAWO TY!')
        #ZDANIA1
        print('Teraz przyszedł czas na test.')
        print('Wiem wiem, nikt nie lubi testów ale trzeba Cię jeszcze podszkolić.')
        print('Teraz nauczysz się pisać podstawowe zwroty.')
        print('1)W alfabecie morsea wszystko piszemy wielką literą.')
        print('2)W alfabecie morsea nie ma przerw między literami.')
        print('I to tyle z teorii, zacznijmy więc.')
        print('Na początku coś prostego, napisz SOS.')
        SOS = input('Napisz SOS: ')
        while SOS != '...---...':
            SOS = input('Ajj no niestety nie, spróbuj jeszcze raz: ')
        print('Teraz pora na KOCHAM CIE.')
        TEST1 = input('Napisz KOCHAM CIE: ')
        while TEST1 != '-.-----.-......----.-....':
            TEST1 = input('Jest to skąplikowany zwrot, spróbuj raz jeszcze: ')
        print('No no jestem pod wrażeniem.')
    else:
        print('No no, sporo umiesz.')
    #ZNAKI INTERPUNKCYJNE
    LEVEL2 = input('Pora na znaki interpunkcyjne.')
    if LEVEL2 != 'Znam ten etap':
        print('Podam Ci dwa podstawowe, wykrzyknik i znak zapytania.')
        print("Jeśli znasz ten znak napisz 'Znam'.")
        yes27 = input('Teraz podam znak zapytania.')
        if yes27 == 'Znam':
            print('To super.')
        else:
            print('Znak zapytania to ..--..')
        QUESTION = input('Napisz znak zapytania: ')
        while QUESTION != '..--..':
            QUESTION = input('No nie, spróbuj jeszcze raz: ')
        yes28 = input('Teraz pora na wykrzyknik.')
        if yes28 == 'Znam':
            print('Okay.')
        else:
            print('Wykrzyknik to .-.--')
    else:
        print('Jestem pod wrażeniem twojej wiedzy', name, '.')
    #KOMENDY SPECJALNE
    LEVEL3 = input('Teraz czas na komendy specjalne.')
    if LEVEL3 != 'Znam ten etap':
        print("Jeśli znasz daną komendę napisz 'Znam'.")
        print('Powodzenia ;)')
        NEGATIVE = input('Napisz wykrzyknik: ')
        while NEGATIVE != '.-.--':
            NEGATIVE = input('Spróbuj jeszcze raz: ')
        print('Teraz komendy specjalne.')
        yes29 = input('Teraz będzie początek kontaktu.')
        if yes29 == 'Znam':
            print('Okay.')
        else:
            print('Początek kontaktu to ...-...-...-')
        START = input('Napisz początek kontaktu: ')
        while START != '...-...-...-':
            START = input('Niestety nie, spróbuj jeszcze raz: ')
        yes30 = input('Teraz koniec kontaktu.')
        if yes30 == 'Znam':
            print('Okay.')
        else:
            print('Koniec kontaktu to ...-.-')
        END = input('Napisz koniec kontaktu: ')
        while END != '...-.-':
            END = input('Niestety nie, spróbuj jeszcze raz: ')
        yes31 = input('Teraz początek nadawania.')
        if yes31 == 'Znam':
            print('Okay.')
        else:
            print('Początek nadawania to -.-.-')
        OPENING = input('Napisz początek nadawania: ')
        while OPENING != '-.-.-':
            OPENING = input('Niestety nie, spróbuj jeszcze raz: ')
        yes32 = input('Pora na koniec nadawania.')
        if yes32 == 'Znam':
            print('Okay.')
        else:
            print('Koniec nadawania to .-.-.')
        ENDING = input('Napisz koniec nadawania: ')
        while ENDING != '.-.-.':
            ENDING = input('Niestety nie, spróbuj jeszcze raz: ')
        yes33 = input('Teraz prośba o powtórzenie.')
        if yes33 == 'Znam':
            print('Okay.')
        else:
            print('Prośba o powtórzenie to ..--..')
        PLEASED = input('Napisz prośbę o powtórzenie: ')
        while PLEASED != '..--..':
            PLEASED = input('Niestety nie, spróbuj jeszcze raz: ')
        yes34 = input('Teraz zrozumiano.')
        if yes34 == 'Znam':
            print('Okay.')
        else:
            print('Zrozumiano to ...-.')
        UNDERSTAND = input('Napisz zrozumiano: ')
        while UNDERSTAND != '...-.':
            UNDERSTAND = input('Niestety nie, spróbuj jeszcze raz: ')
        yes35 = input('Niech teraz będzie czekaj.')
        if yes35 == 'Znam':
            print('Okay.')
        else:
            print('Czekaj to .-...')
        WAIT = input('Napisz czekaj: ')
        while WAIT != '.-...':
            WAIT = input('Niestety nie, spróbuj jeszcze raz: ')
        yes36 = input('Pora na wezwanie.')
        if yes36 == 'Znam':
            print('Okay.')
        else:
            print('Wezwanie to -.-')
        APPEAL = input('Napisz wezwanie: ')
        while APPEAL != '-.-':
            APPEAL = input('Niestety nie, spróbuj jeszcze raz: ')
        yes37 = input('Ostatnie z komend specjalnych to błąd.')
        if yes37 == 'Znam':
            print('Okay.')
        else:
            print('Błąd to po prostu 8 kropek czyli ........')
        MISTAKE = input('Napisz błąd: ')
        while MISTAKE != '........':
            MISTAKE = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Okay, to już wszystko pora na test hihi.')
        #ZADANIA2
        TEST2 = input("Napisz 'Te wezwanie to początek nadawania?'.")
        while TEST2 != '-.-.------.-.-..--..':
            TEST2 = input('To jest ciężkie, spróbuj jeszcze raz: ')
        print('Okay to już większość nauki za nami.')
    else:
        print('Wow, brawo TY!')
    #LICZBY
    LEVEL4 = input('Teraz pouczymy się cyfr.')
    if LEVEL4 != 'Znam ten etap':
        print('Teraz będą liczby, będzie się działo;)')
        yes38 = input('Zaczniemy od 0.')
        if yes38 == 'Znam':
            print('Okay.')
        else:
            print('Zero to ----- LUB -')
        ZERO = input('Napisz zero')
        while ZERO not in['-----', '-']:
            ZERO = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Bardzo dobrze')
        yes39 = input('Teraz 1.')
        if yes39 == 'Znam':
            print('Okay.')
        else:
            print('Cyfra jeden to .---- lub .-')
        ONE = input('Napisz jedynkę: ')
        while ONE not in['.----', '.-']:
            ONE = input('Niestety nie, spróbuj jeszcze raz: ')
        print('No no.')
        yes40 = input('Czas na 2.')
        if yes40 == 'Znam':
            print('Zaraz się okaże.')
        else:
            print('Dwójka to ..--- lub ..-')
        TWO = input('Napisz 2: ')
        while TWO not in['..---', '..-']:
            TWO = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Wow jedziesz tak dalej.')
        yes41 = input('Czas na zmorę byłych gimnazjalistów. Pora na 3.')
        if yes41 == 'Znam':
            print('Skoro tak.')
        else:
            print('Trójka to ...-- lub ...-')
        THREE = input('Napisz 3: ')
        while THREE not in['...--', '...-']:
            THREE = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Bardzo dobrze', name)
        yes42 = input('Przyszedł czas na 4.')
        if yes42 == 'Znam':
            print('Okay.')
        else:
            print('Cztery to ....-')
        FOUR = input('Napisz 4: ')
        while FOUR != '....-':
            FOUR = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Bardzo dobrze.')
        yes43 = input('Teraz będzie 5.')
        if yes43 == 'Znam':
            print('Okay.')
        else:
            print('Piątka to po prostu 5 kropek czyli .....')
        FIVE = input('Napisz 5: ')
        while FIVE != '.....':
            FIVE = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Bardzo dobrze.')
        yes44 = input('Teraz czas na 6.')
        if yes44 == 'Znam':
            print('Niech będzie.')
        else:
            print('6 to -....')
        SIX = input('Napisz 6: ')
        while SIX != '-....':
            SIX = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Coraz lepiej.')
        yes45 = input('Teraz najwyższy czas na liczbę pecha czas na 7.')
        if yes45 == 'Znam':
            print('No skoro tak.')
        else:
            print('7 to --... lub -...')
        SEVEN = input('Teraz napisz 7: ')
        while SEVEN not in['--...', '-...']:
            SEVEN = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Coraz bliżej końca.')
        yes46 = input('Teraz będzie 8.')
        if yes46 == 'Znam':
            print('Skoro tak.')
        else:
            print('8 to ---.. lub -..')
        EIGHT = input('Napisz 8: ')
        while EIGHT not in['---..', '-..']:
            EIGHT = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Jestem pod ogromnym wrażeniem.')
        yes47 = input('To dobry moment na ostatnią cyfrę na 9.')
        if yes47 == 'Znam':
            print('Niech Ci będzie.')
        else:
            print('9 TO ----. lub -.')
        NINE = input('Napisz 9: ')
        while NINE not in['----.', '-.']:
            NINE = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Teraz umiesz już wszystko'. name)
    else:
        print('Naprawdę dużo umiesz.')
    #TEST
    LEVEL5 = input('Tutaj jest test z całej wiedzy.')
    if LEVEL5 != 'ADMIN':
        TEST3 = input("Napisz 'Ten tu jest 89?'")
        while TEST3 not in[ '-.-.-..-.---....----..----.', '-.-.-..-.---....--..-.']:
            TEST3 = input('Niestety nie, pamiętaj, że możesz to na dwa sposoby zapisać: ')
        print('Superaśnie!')
        print('Odpowiedz na to pytanie.')
        TEST4 = input('W którym roku była bitwa pod Grunwaldem?')
        while TEST4 not in['.----....-.---------', '.-....-.--']:
            TEST4 = input('Niestety nie, spróbuj jeszcze raz: ')
        print('ŚWIETNIE!')
        TEST5 = input("Napisz 'Dzisiaj jest rok 2020'")
        while TEST5 not in['-..--..........-.---.---....-.-.----.-..--------..--------', '-..--..........-.---.---....-.-.----.-..--..--']:
            TEST5 = input('Niestety nie, spróbuj jeszcze raz: ')
        print('Nice ostatni teraz.')
        TEST6 = input("Napisz 'Mam kocyk w lamy'")
        while TEST6 != '--.----.-----.-.-.---.-.--.-...----.--':
            TEST6 = input('Niestety nie, spróbuj raz jeszcze: ')
        print('Bardzo dobrze')
    else:
        print('To już koniec!')
        print('Mam nadzieję, że Ci się spodobało.')
        print('Jeśli masz jakieś uwagi co do programu, coś nie działa, lub chociażby chcesz dać mi znać co o tym myślisz napisz do mnie.')
        print('Mój email to: maciek.drozdziel@op.pl')
        print('Dziękuję za uwagę.')
else:
    print('To wielka szkoda :(')
#ZAMYKANIE PROGRAMU
input('\n\nAby zakończyć program, naciśnij klawisz ENTER')

