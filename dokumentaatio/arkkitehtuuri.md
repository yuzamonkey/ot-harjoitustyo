## Arkkitehtuurikuvaus

### Rakenne

Sovellus noudattaa kolmikerrosarkkitehtuuria:
- Käyttöliittymä (UI)
- Sovelluslogiikka (Services)
- Tiedon talletus (Repositories)

Pakkaus Entities sisältää sovelluksen käyttämiä luokkia. Pakkaus Utils sisältää mm. vakioita ja värejä, joita voi hyödyntää muissa pakkauksissa.

![pakkauskaavio](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/package_diagram.svg?raw=true)

#### Entities

![luokkakaavio](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/class_diagram.svg?raw=true)

## Käyttöliittymä

Sovellus avautuu näkymään, josta käyttäjä voi valita uuden tiedoston luomisen tai tallennetun avaamisen. Molemmista päädytään näkymään, jossa käyttäjä voi suorittaa navigaatiopalkissa esitettyjä toimintoja

## Päätoiminnallisuudet

## Tiedostojen tallentaminen ja tallennettujen tiedostojen avaaminen