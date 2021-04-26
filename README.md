# Nuotinkirjoitusohjelma

Nuotinkirjoitusohjelmalla voi kirjoittaa ja toistaa sävelmiä. Projekti on harjoitustyö HY:n kurssille Ohjelmistotekniikka.

[Release 1 (viikko 5)](https://github.com/yuzamonkey/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio
[Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)

[Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita aloitustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot
### Ohjelman suoritaminen

```bash
poetry run invoke start
```

### Tarvittavien hakemistojen luonti

```bash
poetry run invoke build
```
Projektin juuressa tulisi komennon jälkeen olla hakemisto _data_, jonka sisällä hakemisto _scores_

### Testaus

```bash
poetry run invoke test
```

### Testikattavuus

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

## Sovelluksen tila ja tulevaisuus (26.4.2021)
Lähes kaikki toiminnallisuudet ovat valmiit. Seuraavaksi koodin refaktorointia ja UI:n parantelua. 
