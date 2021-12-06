from pizzas import pizza_order, address
from sounds import asking, record_voice, speaker, yes_no
import warnings
import pandas as pd
import time

warnings.filterwarnings(action="ignore")

prices = {
    "marinara": 10,
    "margherita": 15,
    "hawajska": 17,
    "parma": 18,
    "rukola": 20,
    "funghi": 20,
    "diavola": 21,
    "capricciosa": 22,
    "vegetariana": 23,
}

pizza_list = [
    "marinara",
    "margherita",
    "hawajska",
    "parma",
    "rukola",
    "funghi",
    "diavola",
    "capricciosa",
    "vegetariana",
]

price_list = [10, 15, 17, 18, 20, 20, 21, 22, 23]

ingredient_list = [
    "sos pomidorowy, ząbek czosnku, (bez sera mozarella)",
    "sos pomidorowy, mozarella, parmezan",
    "sos pomidorowy, mozarella, szynka gotowana, ananas, parmezan",
    "sos pomidorowy, mozarella, szynka parmeńska, karczochy, parmezan",
    "sos pomidorowy, mozarella, rukola, szynka parmeńska, pomidorki cherry, parmezan",
    "sos pomidorowy, mozarella, pieczarki, parmezan",
    "sos pomidorowy, mozarella, spinata (włoskie salami pikantne), papryczki jalapeno",
    "sos pomidorowy, mozarella, szynka gotowana, pieczarki, czarne oliwki, parmezan",
    "sos pomidorowy, mozarella, czarne oliwki, pieczarki, kukurydza",
]

MENU = pd.DataFrame({"Pizza": pizza_list, "Składniki": ingredient_list, "Cena": price_list})

greeting = "Dzień dobry, witamy w pizzerii polsko-japońskiej!"
pizza_question = "Jaką pizzę sobie życzysz?"
address_question = "Podaj proszę swój adres?"


def order():
    order_list = []
    cost = 0
    costs = []
    print(MENU.head(20))
    speaker(greeting)

    while True:
        pizza = asking(pizza_question, pizza_order)
        order_list.append(pizza)
        costs.append(prices[pizza])
        cost += prices[pizza]
        speaker("Czy chcesz zamówić coś jeszcze?")
        confirmation = yes_no(record_voice())
        if confirmation == True:
            continue
        else:
            speaker("Przechodzę do finalizacji zamówienia.")
            break

    customer_address = asking(address_question, address)

    order_total = pd.DataFrame({"Zamowienie": order_list, "Cena": costs})
    print(order_total.head(20))
    print(f"Adres dostawy to: {customer_address}")
    speaker(
        f"Twoje zamówienie oraz adres jest widoczne na ekranie. Za całość zapłacisz {str(cost)} złotych. Smacznego, życzymy miłego dnia!"
    )
    time.sleep(10)


if __name__ == "__main__":
    order()
