import morfeusz2

def analiza_morfologiczna(s):   #niestety dziala tylko z poprawnie zlozonymi slowami ; zaprojektowalem to tak zeby bralo tylko pierwsze slowo ze stringa poniewaz wczytywanie zapisuje mi liste slow i chce przekazywac slowa po kolei
    morf = morfeusz2.Morfeusz()
    lemizacja= morf.analyse(s)  #OTRZYMUJE LISTE a w  niej tuple a w nim tuple to co nas interesuje jest gleboko zakopane w tuple...
    cos=[x[2] for x in lemizacja]   #wybieramy w tuple element w ktorym jest kolejny tuple
    cos2=[y[1] for y in cos]    # wskazujemy na rubryke z lematem slowa ## nwm jak ominac to i wziac tylko pierwszy element
    print(cos2[0])


s= input()
analiza_morfologiczna(s)

