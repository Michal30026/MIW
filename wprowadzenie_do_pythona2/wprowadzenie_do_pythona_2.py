# Zadanie 1

a_list  = [ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ]
b_list  = [ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ]
ab_list  = []

def  zad1 ( a_list , b_list ):
    ab_list  = [ i  dla  i , j  w  wyliczeniu ( a_list ), jeśli  i  %  2  ==  0 ]
    ab_list  + = [ i  dla  i , j  w  wyliczeniu ( b_list ), jeśli  i  %  2  ==  1 ]
    powrót  drukuj ( ab_list )


zad1 ( a_list , b_list )


# Zadanie 2

def  zad2 ( data_text ):
    length  =  len ( data_text )
    litery  =  lista ( tekst_tekstu )
    big_letters  =  tekst_ danych . górny ()
    small_letters  =  tekst_ danych . niższe ()
    dict  = {
        „długość” : długość ,
        „litery” : litery ,
        „big_letters” : big_letters ,
        „small_letters” : small_letters
    }
     druk zwrotny ( dyktafon )


zad2 ( „Volleyball” )


# Zadanie 3

def  zad3 ( tekst , list ):
    wynik  =  tekst . zastąpić ( list , '' )
    powrót  drukuj ( wynik )


zad3 ( „kajak” , „k” )


# Zadanie 4

def  zad4 ( stopnie_celsjusza , typ temperatury ):
    if  temperature_type  ==  'Fahrenheit' :
        wynik  = ( stopnie_celsjusza  *  9  /  5 ) +  32
        powrót  drukuj ( wynik )
    elif  temperature_type  ==  'Rankine' :
        wynik  = ( stopnie_celsjusza  *  9  /  5 ) +  491,67
        powrót  drukuj ( wynik )
    elif  temperature_type  ==  'Kelvin' :
        wynik  =  stopnie_celsjusza  +  273,15
        powrót  drukuj ( wynik )
    inaczej :
        powrót  drukuj ( „Błąd! Proszę podać prawidłowy typ temperatury” )


zad4 ( 4 , „Fahrenheit” )
zad4 ( 4 , „Rankine” )
zad4 ( 4 , „Kelvin” )
zad4 ( 4 , „???” )


# Zadanie 5

 Kalkulator klasy :
    def  add ( a , b ):
        wynik  =  a  +  b
        powrót  drukuj ( wynik )

     różnica def ( a , b ):
        wynik  =  a  -  b
        powrót  drukuj ( wynik )

    def  pomnóż ( a , b ):
        wynik  =  a  *  b
        powrót  drukuj ( wynik )

    def  divide ( a , b ):
        wynik  =  a  /  b
        powrót  drukuj ( wynik )


Kalkulator . dodaj ( 1 , 1 )
Kalkulator . różnica ( 6 , 2 )
Kalkulator . pomnożyć ( 3 , 2 )
Kalkulator . podział ( 16 , 2 )


# Zadanie 6

klasa  ScienceCalculator ( kalkulator ):
     potęgowanie def ( a , b ):
        wynik  =  a  **  b
        powrót  drukuj ( wynik )


ScienceCalculator . potęgowanie ( 2 , 4 )


# Zadanie 7

def ć w7 ( tekst ):
    tekst_od_ty ł u  =  tekst [:: - 1 ]
    powrót  drukuj ( tekst_od_ty ł u )

ć w7 ( „koteł” )



# Zadanie 8-9

z  file_manager  import  FileManager

plik  =  Menedżer plików ( "plik.txt" )

Menedżer plików . read_file ( plik )
Menedżer plików . update_file ( plik , "oraz tekst, który został dopisany" )
Menedżer plików . read_file ( plik )