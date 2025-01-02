zadanie 1
```python 
from folder_aplikacji.models import Osoba
osoby = Osoba.objects.all()
print(osoby)
```

zadanie 2
```python 
osoba = Osoba.objects.get(id = 3)
print(osoba)
```

zadanie 3
```python
osoba_z_B = Osoba.objects.filter(imie__startswith = 'B' )
print(osoba_z_B)
```

zadanie 4
```python
stanowiska = Osoba.objects.values('stanowisko').distinct()
print(stanowiska)
```

zadanie 5
``` python
from folder_aplikacji.models import Stanowisko
Stanowisko.objects.values_list('nazwa', flat = True).order_by("-nazwa")
```

zadanie 6
```python 
Osoba.objects.create(imie = 'Maja', nazwisko = 'Horoszczak', plec = 1, stanowisko= Stanowisko.objects.get(id= 5))
```