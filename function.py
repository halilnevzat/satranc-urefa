import random
import sys

#// its the place that "makamlar"  have words and meanings in it .*// 

makamlar = ['makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7','makam1','maakm2','makam3','makam4','makam5','makam6','makam7']
oyuncubir = 0
oyuncuiki = 0

#zar is dice
def zar():
    return random.randint(1, 6)

#player1 function
def oyuncu1():
    global oyuncubir
    while True:
        print('oyuncu birin değeri :', oyuncubir, makamlar[oyuncubir])
        oyuncubir = oyuncubir + zar()
        # these if's is the arrows and snakes
        if oyuncubir == 2:
            print('yılana denk geldin yeni makamın ıvırzıvır')
            oyuncubir = 3
            print('yeni değerin :', oyuncubir)
        if oyuncubir == 20:
            print('yılana denk geldin yeni makamın ıvırzıvır')
            oyuncubir = 3
            print('yeni değerin :', oyuncubir)
        if oyuncubir == 98:
            print('yılana denk geldin yeni makamın ıvırzıvır')
            oyuncubir = 3
            print('yeni değerin :', oyuncubir)
        if oyuncubir == 97:
            print('yılana denk geldin yeni makamın ıvırzıvır ')
            oyuncubir = 3
            print('yeni değerin :', oyuncubir)
        if oyuncubir == 85:
            print('yılana denk geldin yeni makamın ıvırzıvır ')
            oyuncubir = 3
            print('yeni değerin :', oyuncubir)
        if oyuncubir == 4:
            print('yılana denk geldin yeni makamın ıvırzıvır ')
            oyuncubir = 1
            print('yeni değerin :', oyuncubir)
        if oyuncubir > 100:
            print("oyuncu bir kazandı")
            oyunbitti1()
        seçim()

#player 2 function
def oyuncu2():
    global oyuncuiki
    while True:
        print('oyuncu ikinin değeri :', oyuncuiki,makamlar[oyuncuiki])
        oyuncuiki = oyuncuiki + zar()
        if oyuncuiki > 100:
            print("oyuncu bir kazandı")
            oyunbitti2()
        seçim()

# shows who won
def oyunbitti1():
    print('oyun bitti kazanan oyuncu1')
    sys.exit()
def oyunbitti2():
    print('oyun bitti kazanan oyuncu2')
    sys.exit()
#its the choosing place, if its player 1 then hit 1, if its player 2 hit 2.
def seçim():
    x = int(input("oyuncu1 için 1e oyuncu2 için 2ye bas"))
    if x == 1:
     oyuncu1()
    if x == 2:
     oyuncu2()

     #if you not pressed 1 or 2 it asks press 1 or 2 only.
    else: print('lütfen sadece 1 veya 2 ye basın')
seçim()




