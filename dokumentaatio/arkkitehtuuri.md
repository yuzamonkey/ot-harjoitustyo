## Arkkitehtuurikuvaus

Sovellus noudattaa kolmikerrosarkkitehtuuria:
- Käyttöliittymä (UI)
- Sovelluslogiikka (Services)
- Tiedon talletus (Repositories)

Pakkaus Entities sisältää sovelluksen käyttämiä luokkia. Pakkaus Utils sisältää mm. vakioita ja värejä, joita voi hyödyntää muissa pakkauksissa.

### Sovelluslogiikka
Alustava luokkakaavio perustoiminnallisuuksia varten (Kaaviossa Bar on koodissa Measure, sillä pylint ei salli nimeä bar):

![luokkakaavio](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/class_diagram.svg?raw=true)