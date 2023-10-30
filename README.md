# django-menot
Menojen seurantaohjelma (Django-harjoitteluprojekti)

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
