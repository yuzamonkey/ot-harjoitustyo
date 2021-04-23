## Arkkitehtuurikuvaus

### Rakenne

Sovellus noudattaa kolmikerrosarkkitehtuuria:
- Käyttöliittymä (UI)
- Sovelluslogiikka (Services)
- Tiedon talletus (Repositories)

Pakkaus Entities sisältää sovelluksen käyttämiä tietokohteita. Pakkaus Utils sisältää mm. vakioita ja värejä, joita muut pakkaukset hyödyntävät.

![pakkauskaavio](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/package_diagram.svg?raw=true)

### Sovelluslogiikka

Sovelluksen tietokohteet sijaitsevat pakkauksessa Entities:
![luokkakaavio](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/class_diagram.svg?raw=true)

Services pakkauksessa on tällä hetkellä kaksi luokkaa toiminnallisuuksia varten: FileService ja ScoreService. FileService vastaa tiedostojen luonnista, tallennuksesta ja tallennettujen tiedostojen hakemisesta. ScoreService vastaa nuotin muokkauksesta. Toistoa varten luodaan luokka PlaybackService.

### Käyttöliittymä

Sovellus avautuu näkymään, josta käyttäjä voi valita uuden tiedoston luomisen tai tallennetun avaamisen. Molemmista päädytään näkymään, jossa käyttäjä voi suorittaa navigaatiopalkissa esitettyjä toimintoja.

### Päätoiminnallisuudet

### Tiedostojen tallentaminen ja tallennettujen tiedostojen avaaminen

Scoret tallennetaan luokkina käyttämällä pythonin pickle moduulia score_repository-luokassa. Tiedostot tallentuvat projektin data-hakemiston alle, joista niitä voi hakea myös editoitavaksi.