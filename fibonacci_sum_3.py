""" Ciąg Tribonacciego.
Oblicza wyrazy ciągu Tribonacciego."""

import sys 

print(''' Ciąg Tribonacciego
      Ciąg Tribonacciego zaczyna się od 0, 1 i 2 a kolejny element 
      jest sumą trzech poprzednich. Ciąg nie ma końca:''')

while True:     # Główna pętla programu.
    while True:     # Pytaj, dopóki użytkownik nie wpisze odpowiedniej wartości.
        print('Wpisz n-ty wyraz, do którego chcesz obliczyć ')
        print('ciąg Tribonacciego (np. 5, 50, 9999), lub KONIEC, by wyjść:')
        response = input('> ').upper()

        if response == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break   # Wyjdź z pętli, gdy użytkownik poda odpowiednią wartość.

        print('Podaj liczbę większą od 0 lub KONIEC.')
    print()

    # Obsługa poszczególnych przypadków, gdy użytkownik poda 1 lub 2 lub 3:
    if nth == 1:
        print('0')
        print()
        print('#1 wyraz ciągu Tribonacciego to 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('#2 wyraz ciągu Tribonacciego to 1.')
        continue
    elif nth == 3:
        print('0, 1, 2')
        print()
        print('#3 wyraz ciągu Tribonacciego to 2.')
    # Wyświetl ostrzeżenie, gdy użytkownik poda bardzo dużą liczbę:
    if nth >= 10_000:
        print('UWAGA: Wyświetlanie wszystkich wyrazów ciągu na ekranie')
        print('zajmie chwilę. Jeśli chcesz zatrzymać program przed wyświetleniem')
        print('wszystkich elementów, naciśnij Ctrl+C.')
        input('Wciśnij Enter, by rozpocząć...')

    # Oblicz n-ty wyraz ciągu Tribonacciego:
    secondToLastNumber = 0
    lastNumber = 1
    thirdNumber = 2
    fibNumberCalculated = 3
    print('0, 1, 2, ', end='')     # Wyświetl pierwsze dwa elementy ciągu Fibonacciego.

    # Wyświetl kolejne wyrazy ciągu Tribonacciego:
    while True:
        nextNumber = secondToLastNumber + lastNumber + thirdNumber
        fibNumberCalculated += 1

        # Wyświetl kolejną liczbę ciągu:
        print(nextNumber, end='')

        # Sprawdź, czy znaleźliśmy n-ty element, do którego użytkownik chciał obliczyć ciąg:
        if fibNumberCalculated == nth:
            print()
            print()
            print('#', fibNumberCalculated, ' wyraz ciągu Tribonacciego', 
                  'to ', nextNumber, sep='')
            break

        # Wyświetl przecinek między elementami ciągu:
        print(', ', end='')

        # Przestaw ostatnie dwie liczby:
        secondToLastNumber = lastNumber
        lastNumber = thirdNumber
        thirdNumber = nextNumber 
        