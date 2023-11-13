# django-menot
Menojen seurantaohjelma (Django-harjoitteluprojekti)

## Asentaminen

1. Luo virtuaaliympäristö:

       python -m venv venv

2. Aktivoi virtuaaliympäristö

       . venv/bin/activate   # Linuxissa tai Macissä
       .\venv\Scripts\activate.ps1  # Windows (PowerShell)

3. Asenna Django

       pip install django

## Kehittäminen

### Kielikäännökset (suomentaminen)

Poimi ensin uudet käännettävät tekstit koodista PO-tiedostoihin
(locale/fi/django.po) ajamalla:

    python manage.py makemessages --ignore venv --locale fi

Sen jälkeen tee suomennokset komennon luomaan tai päivittämään
`django.po`-tiedostoon.  Alkuperäinen (englanninkielinen) teksti on
rivillä, joka alkaa `msgid` ja käännös tulee sen alapuolelle riville,
joka alkaa `msgstr`.

Django lukee käännökset MO-tiedostoista (Message Object). Saat
käännettyä PO-tiedostot MO-tiedostoiksi komennolla:

    python manage.py compilemessages --ignore venv

## Modelit

* Tili (Account)
* Tilitapahtuma (Transaction)
  - Tyyppi: Tulo, Meno
  - Tila: Tuleva, Tapahtunut
  - Tositteet
* Dokumentti (Document)
  - Käytännössä tiedosto, esim. lasku tai kuitti
* Kategoria (Category)
  - Esim. autoilu, polttoaineet, säästöt, koti, jne.
* Käyttäjä (User) (Tulee Djangosta)
