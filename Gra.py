#importy
import time

#intro
print("===========================================")
print("Witam w grze Wybieraj aby przetrwac")
print("Dostaniesz kilka opcji do wyboru")
print("===========================================")
print()
#wybór pomocy
def wybory():
    print("1.Info")
    print("2.Graj")
    print("3.Wyjdz z gry")
print(wybory())
wybor_pomocy = int(input("Co wybierasz?: "))
print()

#dzialania wyborów
if wybor_pomocy == 1:
    print("dobrze, oto informacje o grze:")
    time.sleep(1)
    print("Autor: Ksawery")
    print("Czas tworzenia gry: ") #DO WYPEŁNIENIA!!! zaczęto tworzenie 15.09.2023
    print("Info o grze: To jest PROTOTYP tej gry, wiec kilka rzeczy mogą byc błedne"
          " warto pamiec, ze trzeba sie kilka razy zastanowic, zanim sie dokona wyboru"
          " bo zły wybór wywala z gry!")
    print()
    pytanie = input("Gotowy do gry? (tak,nie): ")
    if pytanie == "tak":
        print("No to miłego grania :D")
        print("PS: Jezeli opuscisz gre, stracisz wszystkie postępy")
        print()
    else:
        quit()
elif wybor_pomocy == 2:
    print("No to miłego grania :D")
    print("PS: Jezeli opuscisz gre, stracisz wszystkie postępy")
    print()
elif wybor_pomocy == 3:
    print("No to dowidzenia!")
    time.sleep(1)
    print("Wywali cie za 5 sekund")
    time.sleep(5)
    quit()
print()
print("No to zaczynajmy!")

#informacje o graczu
nazwa_gracza = input("Zacznijmy od tego, jak sie nazywasz?: ")
print("Witam cie " + nazwa_gracza)
nazwa_postaci = input(nazwa_gracza + ", jak chcesz żeby twoja postac sie nazywała?: ")
print("Bardzo fajnie!")

#część gry 1
print(nazwa_postaci + ", Chce wyruszyc na wakacje do USA, bierze samolot")

#w usa.
print()
time.sleep(2)
print("'kapitan samolotu w tle'")
print("Panie i panowie przechodzimy przez turbulencje, prosze zapiąc pasy...")
print()
time.sleep(4)
print("==============")
print("czekanie...")
print("===============")
print()
time.sleep(3)
print("==============")
print("światla zgasly...")
print("===============")
print()
print(nazwa_postaci + ", jest przestraszony(-a)")
time.sleep(3)
print("==============")
print("silniki zgasly...")
print("===============")
print()
time.sleep(3)
print("==============")
print("SAMOLOT SPADA...")
print("===============")
time.sleep(2)

#samotna wyspa
print("=============================")
print(nazwa_postaci + ", budzi sie na jakies wyspie, wszyscy inni zgineli. Co teraz?")
print("==============================")
print()
print("1. Rozgladac sie po wyspie (opuszczasz samolot)")
print("2.Zobaczyc wraki samolotu")
print("3.Zabić sie na miejscu")
odpowiedz = input("Co wybierasz?: ")
if odpowiedz == "1":
    print("Opuszczas samolot")
    print(nazwa_postaci + ", zgubil sie na wyspie, i zginełą z powodu głodu")
    time.sleep(4)
    quit()
if odpowiedz == "2":
    print("=============================")
    print("Wchodzisz do samolotu...")
    print("=============================")
if odpowiedz == "3":
    print("No dobra......")
    time.sleep(2)
    quit()

#w samolocie
print(nazwa_postaci + ", znajduje..")
print("1. Jedzenie")
print("2. Nóż")
time.sleep(1)
print(nazwa_postaci + ", bierze przedmioty i idzie dalej do wyspy")
print()
print("===========")
print("DZIEN 2")
print("===========")
time.sleep(3)
print()
print(nazwa_postaci + ", wstal(-a) glodny(-a), masz wybor")
time.sleep(2)
print()
print("======================================")
print("1. Iśc szukac i zabic zwierzyne")
print("2. Znalesc jakies owoce")
print("3. Jesc trawe")
print("======================================")
odpowiedz = input("Co wybierasz?: ")
#funkcja if
if odpowiedz == "1":
    print(nazwa_postaci + ", poszedl szukac zwierzyny....")
    print("zwierzyna zabila " + nazwa_postaci + ", umierasz!")
    time.sleep(4)
    quit()
elif odpowiedz == "2":
    print(nazwa_postaci + ", znalazl(-a) kilka jablek i malin.")
    print("Brawo " + nazwa_gracza + ", zaszleś(-aś) daleko, teraz bedą coraz gorsze wybory!")
elif odpowiedz == "3":
    print(nazwa_postaci + ", zatrul(-a) sie trawą, odpadasz!")
    time.sleep(2)
    quit()
print()
print(nazwa_postaci + ", sie najadl(-a), lecz " + nazwa_postaci)
print("Probuje sie wydostac z wyspy, bo wie ze tam nie przetrwa zbyt długo, masz wybór")
print("======================================")
print("1. Iśc ciac drzewo na łódke")
print("2. zacząc plywac w strone słonca")
print("3. Zaakceptowac fakt, ze szanse na wydostaniecie sie z wyspy są małe (koniec gry)")
print("======================================")
print()
odpowiedz = input("Co wybierasz?: ")
if odpowiedz == "1":
    print(nazwa_postaci + ", poszla ciac drzewo, przyda sie bardzo")
elif odpowiedz == "2":
    print(nazwa_postaci + ", myślał(-a) ze gdzies dopłynie, rekine go(-ją) zjadły...")
    time.sleep(3)
    quit()
elif odpowiedz == "3":
    print(nazwa_postaci + ", powoli umierala na wyspie")
    print(nazwa_gracza + ", zakonczyles gre, milego dnia!")
    time.sleep(4)
    quit()
print()
print(nazwa_postaci + ", zebrała drzewo, i przeszukała wraki samolotu.")
time.sleep(2)
print("====================")
print("Buduje łodke...")
print("Prosze czekac...")
print("=====================")
print()
time.sleep(3)
