import argostranslate.translate

def Translator_Engine(sentence):
    from_text = "en"
    to_text = "hi"

    a = argostranslate.translate.translate(sentence,from_text,to_text)
    return a

