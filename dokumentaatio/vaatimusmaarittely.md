# Nuotinkirjoitusohjelma 
## Vaatimusmäärittely
### Sovelluksen tarkoitus
  Nuotinkirjoitusohjelmalla voi nuotintaa ja toistaa sävelmiä. Käyttäjä voi valita sävel- ja tahtilajin. Graafista käyttöliittymää ohjataan syöttämällä arvoja tekstikenttiin tai, kurssin aikataulun salliessa, hiirellä raahaamalla elementtejä

### Suunnitellut perustoiminnallisuudet
  - Uuden tiedoston luonti tai tallennetun tiedoston avaus aloitusnäkymästä
  - Käyttäjä voi lisätä ja poistaa nuotteja. Oletusasetuksina avaimena on g-avain, sävellajina c-duuri/a-molli ja tahtilajina 4/4
  - Ohjelma pystyy soittamaan käyttäjän kirjoittaman viisun 
  - Kirjoitetun mestariteoksen pystyy tallentamaan tiedostoon ja tiedostoja voi avata editoitavaksi
  
### Käyttöliittymäluonnos
![luonnos käyttöliittymästä](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/GUI_sketch.jpeg?raw=true)

PaintX-ohjelmalla luotu luonnos GUIsta:
![paintx luonnos](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/gui_sketch.png?raw=true)

### Jatkokehitysideoita
Seuraavista ideoista ainakin ensimmäinen olisi hyvä saada toteutettua kurssin aikataulun puitteissa:
  - Nuottiavaimen, tahtilajin ja sävellajin voi vaihtaa keskellä sävellystä
  - Näppäinoikoteitä sovelluksen nopeampaa käyttöä varten
  - Automaattinen leveys tahdeille niissä olevien nuottien mukaan
  - Yhdistä automaattisesti nuotteja kaarilla ja varsilla
  - Mahdollisuus monimutkaisempiin nuotinnuksiin. Muun muassa epäsymmetriset tahtilajit, dynamiikat ja nuottiarvojen laajentaminen (trioli, kvintoli, etuheleet...)
  - Ohjelma pystyy lukemaan ja exporttamaan .xml-muotoisia tiedostoja
  - Mahdollisuus kirjoittaa useita ääniä samalle nuotille
  - Instrumenttien lisäys
  - Partituurin rakentaminen

