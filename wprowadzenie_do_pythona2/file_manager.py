klasa  FileManager :

    def  __init__ ( self , nazwa_pliku ):
        jaźń . nazwa_pliku  =  nazwa_pliku

    def  read_file ( self ):
        uchwyt  =  open ( self . nazwa_pliku )
        dane  =  uchwyt . read ()
        drukuj ( dane )
        uchwyt . zamknij ()

    def  plik_ aktualizacji ( self , dane_tekstowe ):
        uchwyt  =  open ( self . nazwa_pliku , „a” )
        uchwyt . napisz (dane tekstowe )
        uchwyt . zamknij ()