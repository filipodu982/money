#-*- coding: utf-8 -*-
import math
while True:
    price = input('Podaj liczbę: ')         #Sprawdzam czy dana liczba jest całkowita
    try:
        if isinstance(price, int):
            break
        else:
            raise ValueError
    except:
        print 'Chodziło mi o całkowitą...'
notes = [200, 100, 50, 20, 10, 5, 2, 1]     #Możliwe nominały
rest = []                                   #Tablica, w której trzymane są ilości banknotów/monet danego nominału
for i in notes:
    rest.append(int(price/i))
    price = math.fmod(price, i)             #Reszta z dzielenia kwoty przez dany nominał

print 'Kwotę tą możesz wydać w nominałach: '

for j in range(8):
    print '%rzł x %r' % (int(notes[j]), int(rest[j]))
    
