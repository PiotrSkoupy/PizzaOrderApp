from pizze import pizza_order, adres
from dzwieki import asking, record_voice, speaker, yes_no
import warnings
import pandas as pd
import time
warnings.filterwarnings(action='ignore')

CENY = {'marinara': 10,
        'margherita': 15,
        'hawajska' : 17,
        'parma' : 18,
        'rukola' : 20,
        'funghi' : 20,
        'diavola' : 21,
        'capricciosa' :22,
        'vegetariana' : 23}
RODZAJE = ['marinara', 'margherita','hawajska','parma','rukola','funghi','diavola','capricciosa','vegetariana']
CENY_LISTA = [10,15,17,18,20,20,21,22,23]
SKLADNIKI = ['sos pomidorowy, ząbek czosnku, (bez sera mozarella)', 'sos pomidorowy, mozarella, parmezan', 'sos pomidorowy, mozarella, szynka gotowana, ananas, parmezan',
            'sos pomidorowy, mozarella, szynka parmeńska, karczochy, parmezan', 
            'sos pomidorowy, mozarella, rukola, szynka parmeńska, pomidorki cherry, parmezan',
            'sos pomidorowy, mozarella, pieczarki, parmezan',
            'sos pomidorowy, mozarella, spinata (włoskie salami pikantne), papryczki jalapeno',
            'sos pomidorowy, mozarella, szynka gotowana, pieczarki, czarne oliwki, parmezan',
            'sos pomidorowy, mozarella, czarne oliwki, pieczarki, kukurydza']
MENU = pd.DataFrame({
    'Pizza': RODZAJE,
    'Składniki': SKLADNIKI,
    'Cena': CENY_LISTA
})

POWITANIE= '  Dzień dobry witamy w pizzerii polsko-japońskiej'
PIZZA = 'jaką pizzę sobie życzysz?'
PYTANIE_O_ADRES = ' Podaj proszę swój adres?'
zamowienie =[]
koszt = 0
koszty =[]
print(MENU.head(20))
speaker(POWITANIE)

while True:
    pizza=asking(PIZZA, pizza_order)
    zamowienie.append(pizza)
    koszty.append(CENY[pizza])
    koszt += CENY[pizza]
    speaker('Czy chcesz zamówić coś jeszcze?')
    pytanie = record_voice()
    zatw = yes_no(pytanie)
    if zatw==False:
        break
adres_mieszkania = asking(PYTANIE_O_ADRES, adres)


CALE_ZAMOWIENIE = pd.DataFrame({
    'zamowienie' : zamowienie,
    'cena' : koszty
})
print(CALE_ZAMOWIENIE.head(20))
print(f'Adres dostawy to: {adres_mieszkania}')
speaker(f'Twoje zamówienie oraz adres jest widoczne na ekranie. Za całość zapłacisz {str(koszt)} złotych. Smacznego, życzymy miłego dnia ')
time.sleep(30)




