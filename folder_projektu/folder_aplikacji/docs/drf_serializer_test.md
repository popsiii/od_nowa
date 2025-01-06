from folder_aplikacji.models import Osoba, Stanowisko
from folder_aplikacji.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# nowe obiekty

stanowisko = Stanowisko.objects.create(nazwa = 'chef', opis = "zarzadza kuchcikami") 
osoba = Osoba.objects.create(imie = "David", nazwisko = "Chang", plec = 2, stanowisko = stanowisko)

# inicjalizacja seralizera dla Osoba

osoba_serializer = OsobaSerializer(osoba)
print(osoba_serializer.data)

# {'id' : 12, 'imie' : 'David', 'nazwisko' : 'Chang', 'plec': 'Mężczyzna', 'stanowisko' : stanowisko.id , data_dodania ; osoba.data_dodania}


osoba_json = JSONRenderer().render(osoba_serializer.data)
print(osoba_json) 

# {'id' : 12, 'imie' : 'David', 'nazwisko' : 'Chang', 'plec': 'Mężczyzna', 'stanowisko' : 7, data_dodania ; 2024-01-06}

import io
from io import BytesIO
from rest_framework.parsers import JSONParser

# strumien danych JSON
stream = io.BytesIO(osoba_json)

# pasowanie JSON do slownika
data = JSONParser().parse(stream)

# tworzymy obiekt deserializers dla danych JSON
deserializer = OsobaSerializer(data = data)

# walidacja danych
print(deserializer.is_valid())
print(deserializer.errors)

# true 

# bledne dane
invalid_data = {'imie': 'Izabela' , 'nazwisko': 'Janachowska', 'plec': 'nieznana' , 'stanowisko': stanowisko.id}
invalid_serializer = OsobaSerializer(data= invalid_data)
print(invalid_serializer.is_valid())
print(invalid_serializer.errors)

# False
# {'plec' : [' "Nieznana" is not  avalid choice ']}

# zapis do bazy danych
if deserializer.is_valid() :
    deserializer.save()

# incijacja serializera dla Stanowiska
stanowisko_serializer = StanowiskoSerializer(stanowisko)
print(stanowisko_serializer.data)

# {'id' : 1, 'nazwa' : 'chef' , 'opis' : 'zarzadza kuchcikami'}

# serializacja do JSON 
stanowisko_json = JSONRenderer().render(stanowisko_serializer.data)
print(stanowisko_json)

# {'id' : 1, 'nazwa' : 'chef' , 'opis' : 'zarzadza kuchcikami'} 

# deserializacja z JSON
stream = io.BytesIO(stanowisko_json)
data = JSONParser().parse(stream)

deserializer = StanowiskoSerializer(data= data)

print(deserializer.is_valid())

if deserializer.is_valid() :
    deserializer.save()

