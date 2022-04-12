import nltk

nltk.download('punkt')  ## potrzebne zeby odpalic world_tokenize


def powitanie():
    print('Witaj! Nazywam sie FUWChatbot i służę swoją pomocą! W czym mogę Ci pomóc?')


def wczytywanie_zapytania():
    odpowiedz_uzytkownika = input()
    zapytanie = nltk.word_tokenize(
        odpowiedz_uzytkownika)  # okazuje sie byc lepsza funklcja niz split bo oddziela fajnie interpunkcje od slow
    # usuwanie interpukncji:
    licz = len(zapytanie)
    zapytanie = filter(lambda c: c not in {',','.','?', '!', ':', ';'}, zapytanie)  #funkcja filter filtruje liste z tych znakow
    print(list(zapytanie))  #ona tworzy obiekt i zeby dzialalo trzeba dac list() zrodlo: https://www.simplilearn.com/tutorials/python-tutorial/filter-in-python


powitanie()
wczytywanie_zapytania()
