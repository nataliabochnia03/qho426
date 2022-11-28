print("How many numbers should I sum up?")
numbers_to_sum_up = int(input())
#na razie nie mamy zadnych policzonych numerow, ale musimy je przyrownac do zera, bo odliczenie zawsze zaczynamy od zera xd. Zeby petla dzialala dzialanie musi byc ZAWSZE prawdziwe, czyli logicznie zawsze policzone numer sa na poczatku mniejsze niz numery, ktore mamy do policzenia! gdy bedzie inaczej to petla sie przerywa, bo dzialanie przestaje byc prawdziwe. 
summed = 0
#to jest suma wszystkich numerow razem dodanych. Na poczatku tez musimy zaczac od zera. Jesli bysmy zaczeli np od 2 to to 2 byloby dodane do koncowego wyniku i nie mial by on sensu.
total = 0
#zaczynamy petle. Musi miec ona nawiasy i dwukropek na koncu! i musi sie zgadzac. Traktuj to jako dzialanie matematyczne, a nie zbior slow!!!
while(summed < numbers_to_sum_up):
  #najpierw musimy wstawic 'summed' (policzone numer) zamiast numery do policzenia 'numbers_to_sum_up', bo mamy odliczanie i w pierwszej kolejnosci wyswietli nam sie to zero, ktore przypisalismy wczesniej do 'summed' gdybysmy przypisali 2 albo 3 albo cokolwiek to by sie to wyswietlilo. A wiec mamy 0 z    int(input()) 
  print("Please enter number", summed, "of", numbers_to_sum_up, ":")
  #natepnie musimy dac int(input()) zeby uzytkownik mogl wpisac ten numer, ktory chcemy zsumowac. Od biedy mozna ten caly powyrzszy print wstawic w ponizszy input ale robi sie zbyt chaotycznie i nie jest to dobra praktyka.! 
  number = int(input())

  #0=0+input mozna to tez napisac szybciej 0+=input, przyjmijmy, ze nasz input = 2. Ten 'total' jest naszym pojemnikiem pamieci, on sobie caly czas zatrzymuje te dane i odpowiednio je zmienia. Czyli za drugim razem byloby juz input=input+kolejny input, czyli np 2=2+5 i dopoki by nie przeszedl do nowej lini , to to zadanie nie byloby policzone, ono by sobie po protu bylo w takiej formie (oczywiscie nie wyswietlone) Nastepnie po podliczeniu mamy juz 7=7+kolejny input. I tak dalej i tak dalej. 
  total = total + number
  #za kazdym przejsciem petli mamy o jedno wiecej dzialanie wykonane i zalezy nam na tym, zeby bylo ono w jakis sposob policzone. Do naszego poczatkowego zera, od ktorego zaczelismy odliczanie bedziemy dodawac jeden, bo liczymy tylko jedno dzialanie na raz. Tak jak powyzej wyglada to tak : 0=0+1 nastepnie summed staje sie naszym pojemniczkiem i przechowuje ta jedynke to momentu az bedzie mogl kolejny raz policzyc nowe zadanie i wtedy zaczynamy juz od 1=1+1 pozniej 2=2+2 mozna to tez zapisac w sktrocie 2+=1 
  summed = summed + 1
#nastepnie musimy wydrukowac koncowy wynik. Nasz koncowy wynik to suma wszystkich liczb a wiec 'total' jako, ze jest to nasz "pojemniczek" to przechowuje on caly wynik, zeby bo zobaczyc wystaczy tylko w nawiasie print wstawic total, pamietajmy tylko ze jesli mamy jakies zdanie ktore chcemy wyswietlic urzytkownikowi, w tym wypadku "The total number is" to po tym zdaniu musimy dac przecinek, a nasz total nie moze byc w cudzyslowie, bo wtedy z pojemniczka staje sie tylko zwyklym zdaniem, a tego nie chcemy!:(
print("The total number is", total)

#WAZNE!!!! NIE ZAPOMINAC O POCZATKOWYM PRZYPISYWANIU WSZYSTKIM WARTOSCIA ZERA (JESLI CHCEMY ZACZAC ODLICZENIE OD ZERA) BO POZNIEJ SIE DZIWIE PRZEZ POL GODZINY CZEMY KOD NIE DZIALA, A KOMPUTER NIE WIE CO TO SUMMED ALBO TOTAL JESLI NIE PRZYPISZE DO NIEGO ZADNEJ WARTOSCI!!!!!
