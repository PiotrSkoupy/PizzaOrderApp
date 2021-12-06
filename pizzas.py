from transformers import pipeline
from translate import Translator
import speech_recognition as sr
from sounds import record_voice, speaker, unrecognized


def address():
    while True:
        try:
            address = record_voice()
            response = f"Z tego co rozumiem twój adres to: {address} czy to się zgadza?"
            speaker(response)
            return address
        except Exception as e:
            print(e)
            unrecognized()


def pizza_classifier(text_input):
    translator = Translator(to_lang="en", from_lang="pl")
    translation = str(translator.translate(text_input))
    classifier = pipeline("zero-shot-classification")
    result = classifier(
        translation,
        candidate_labels=[
            "tomato sauce, garlic clove (without mozzarella cheese), MARINARA",
            "tomato sauce, mozzarella, and Parmesan, margherita",
            "tomato sauce, mozzarella, cooked ham, pineapple, and Parmesan, hawaian",
            "tomato sauce, mozzarella, Parma ham, artichokes, and Parmesan, parma"
            "tomato sauce, mozzarella, arugula, Parma ham, cherry tomatoes, and Parmesan, rucola",
            "tomato sauce, mozzarella, champignons, and Parmesan, MUSHROOMS",
            "tomato sauce, mozzarella, spinata (Italian spicy salami), and jalapeno peppers, DEVIL ",
            "tomato sauce, mozzarella, cooked ham, mushrooms, black olives, and Parmesan,CAPRICIOUS ",
            "tomato sauce, mozzarella, black olives, champignons, and corn, VEGETARIAN ",
        ],
    )

    pizza_dict = {
        "tomato sauce, garlic clove (without mozzarella cheese), MARINARA": "marinara",
        "tomato sauce, mozzarella, and Parmesan, margherita": "margherita",
        "tomato sauce, mozzarella, cooked ham, pineapple, and Parmesan, hawaian": "hawajska",
        "tomato sauce, mozzarella, Parma ham, artichokes, and Parmesan, parma": "parma",
        "tomato sauce, mozzarella, arugula, Parma ham, cherry tomatoes, and Parmesan, rucola": "rukola",
        "tomato sauce, mozzarella, champignons, and Parmesan, MUSHROOMS": "funghi",
        "tomato sauce, mozzarella, spinata (Italian spicy salami), and jalapeno peppers, DEVIL ": "diavola",
        "tomato sauce, mozzarella, cooked ham, mushrooms, black olives, and Parmesan,CAPRICIOUS ": "capricciosa",
        "tomato sauce, mozzarella, black olives, champignons, and corn, VEGETARIAN ": "vegetariana",
    }

    scores = result["scores"]
    labels = result["labels"]
    response = dict(zip(labels, scores))
    max_key = max(response, key=response.get)
    return pizza_dict[max_key]


def pizza_order():
    while True:
        try:
            audio = record_voice()
            ordered_pizza = pizza_classifier(audio)
            response = f"Z tego co rozumiem to poszukiwana przez Ciebie pizza to: {ordered_pizza} czy to się zgadza?"
            speaker(response)
            return ordered_pizza
        except Exception as e:
            print(e)
            unrecognized()
