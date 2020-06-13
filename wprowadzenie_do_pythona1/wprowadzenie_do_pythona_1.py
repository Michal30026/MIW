# zadanie 1
drukuj ( „Przypisanie do zmiennej” )
zmienna  =  "Lorem ipsum to roboczy tekst używany do celów projektowych, zwykle do prezentacji kroju pisma, składu, układu kolumn, zawartości zestawu, typografii itd."

# zadanie 2
imie  =  "Michał"
nazwisko  =  "Uciński"

litera_1  =  imie [ 2 ]
litera_2  =  nazwisko [ 4 ]

liczba_liter_1  =  zmienna . liczyć ( litera_1 )
liczba_liter_2  =  zmienna . liczba ( litera_2 )

print ( "W tekście jest {0} litr {1} oraz {2} litr {3}" . format ( liczba_liter_1 , litera_1 , liczba_liter_2 , litera_2 ))

# zadanie 4
zmienna_typu_string  =  "Lorem Ipsum"

print ( dir ( zmienna_typu_string ))

# zadanie 5
print( „Extended Slices dla Michał Uciński:” )
print ( nazwisko [:: - 1 ]. capitalize (), imie [:: - 1 ]. capitalize ())

# zadanie 6-7
lista1  = []
o  x  w  przedziale ( 1 , 11 )
    lista1 . append ( x )
drukuj ( „Lista” , lista1 )

lista2  = []
dla  x  na  liście1 [ 5 :]:
    lista2 . append ( x )
    lista1 . usuń ( x )

drukuj ( „Listy podzielone:” )
drukuj ( lista1 , lista2 )
lista1 . przedłużyć ( lista2 )

print ( „Połączone:” , lista1 )
lista1 . wstaw ( 0 , 0 )
print ( „Dodane zero:” , lista1 )
lista1 . do tyłu ()
drukuj ( „Odwrócona:” , lista1 )

# zadanie 10
listatel  = [ 1 , 2 , 2 , 5 , 5 , 7 , 7 , 9 , 9 , 10 , 10 , 12 , 12 ]
unikatowe  =  set ( listatel )
print ( „Lista dostępna:” , listatel )
drukuj ( „Lista unikatowa” , unikatowe )

# zadanie 11
listx  = []
o  x  w  przedziale ( 1 , 11 , 1 )
    listx . append ( x )
drukuj ( „Lista 1-10” , listx )

# zadanie 12
listy  = []
dla  X  w  zakresie ( 100 , 19 , - 5 ):
    listy . append ( x )
drukuj ( „Lista 100-20” , listy )