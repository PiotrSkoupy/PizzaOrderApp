from transformers import pipeline
from translate import Translator
import speech_recognition as sr
from dzwieki import record_voice, speaker, unrecognized



def adres():
    while True:
        try:
            adres = record_voice()
            moj_tekst = f'Z tego co rozumiem twój adres to: {adres} czy to się zgadza?' 
            speaker(moj_tekst)
            return adres
        except Exception as e:
            print(e)
            unrecognized()


def klasyfikacja_pizzy(tekst):
    translator = Translator(to_lang='en', from_lang='pl')
    translation = str(translator.translate(tekst))
    classifier = pipeline('zero-shot-classification')
    wynik=classifier(
        translation,
        candidate_labels = ['tomato sauce, garlic clove (without mozzarella cheese), MARINARA',
         'tomato sauce, mozzarella, and Parmesan, margherita', 
         'tomato sauce, mozzarella, cooked ham, pineapple, and Parmesan, hawaian', 
         'tomato sauce, mozzarella, Parma ham, artichokes, and Parmesan, parma'
         'tomato sauce, mozzarella, arugula, Parma ham, cherry tomatoes, and Parmesan, rucola',
         'tomato sauce, mozzarella, champignons, and Parmesan, MUSHROOMS',
         'tomato sauce, mozzarella, spinata (Italian spicy salami), and jalapeno peppers, DEVIL ',
         'tomato sauce, mozzarella, cooked ham, mushrooms, black olives, and Parmesan,CAPRICIOUS ',
         'tomato sauce, mozzarella, black olives, champignons, and corn, VEGETARIAN '],  
    )

    SLOWNIK_PIZZY = {'tomato sauce, garlic clove (without mozzarella cheese), MARINARA':'marinara',
                    'tomato sauce, mozzarella, and Parmesan, margherita':'margherita',
                    'tomato sauce, mozzarella, cooked ham, pineapple, and Parmesan, hawaian':'hawajska',
                    'tomato sauce, mozzarella, Parma ham, artichokes, and Parmesan, parma':'parma',
                    'tomato sauce, mozzarella, arugula, Parma ham, cherry tomatoes, and Parmesan, rucola':'rukola',
                    'tomato sauce, mozzarella, champignons, and Parmesan, MUSHROOMS':'funghi',
                    'tomato sauce, mozzarella, spinata (Italian spicy salami), and jalapeno peppers, DEVIL ':'diavola',
                    'tomato sauce, mozzarella, cooked ham, mushrooms, black olives, and Parmesan,CAPRICIOUS ':'capricciosa',
                    'tomato sauce, mozzarella, black olives, champignons, and corn, VEGETARIAN ': 'vegetariana'}

    scores = wynik['scores']
    labele = wynik['labels']
    res = dict(zip(labele,scores))
    max_key = max(res, key=res.get)
    return SLOWNIK_PIZZY[max_key]

def pizza_order():
    while True:
        try:
            audio = record_voice()
            ordered_pizza = klasyfikacja_pizzy(audio)
            moj_tekst = f'Z tego co rozumiem to poszukiwana przez Ciebie pizza to: {ordered_pizza} czy to się zgadza?' 
            speaker(moj_tekst)
            return ordered_pizza
        except Exception as e:
            unrecognized()