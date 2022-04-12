import nltk
import morfeusz2

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



def analiza_morfologiczna(s):   #niestety dziala tylko z poprawnie zlozonymi slowami ; zaprojektowalem to tak zeby bralo tylko pierwsze slowo ze stringa poniewaz wczytywanie zapisuje mi liste slow i chce przekazywac slowa po kolei
    morf = morfeusz2.Morfeusz()
    lemizacja= morf.analyse(s)  #OTRZYMUJE LISTE a w  niej tuple a w nim tuple to co nas interesuje jest gleboko zakopane w tuple...
    cos=[x[2] for x in lemizacja]   #wybieramy w tuple element w ktorym jest kolejny tuple
    cos2=[y[1] for y in cos]    # wskazujemy na rubryke z lematem slowa ## nwm jak ominac to i wziac tylko pierwszy element
    print(cos2[0])


s= input()
analiza_morfologiczna(s)

