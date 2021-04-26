# Arkkitehtuurikuvaus

## Rakenne

Sovellus noudattaa kolmikerrosarkkitehtuuria:
- Käyttöliittymä (UI)
- Sovelluslogiikka (Services)
- Tiedon talletus (Repositories)

Pakkaus Entities sisältää sovelluksen käyttämiä tietokohteita. Pakkaus Utils sisältää mm. vakioita ja värejä, joita muut pakkaukset hyödyntävät.

![pakkauskaavio](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/package_diagram.svg?raw=true)

## Sovelluslogiikka

Sovelluksen tietokohteet sijaitsevat pakkauksessa Entities:

![luokkakaavio](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/class_diagram.svg?raw=true)

Services pakkauksessa on kolme luokkaa toiminnallisuuksia varten: FileService, ScoreService ja PlaybackService. FileService vastaa tiedostojen luonnista, tallennuksesta ja tallennettujen tiedostojen hakemisesta. ScoreService vastaa nuotin muokkauksesta. Luokka PlaybackService on editoitavana olevan tiedoston toistoa varten.

## Käyttöliittymä

Sovellus avautuu näkymään, josta käyttäjä voi valita uuden tiedoston luomisen tai tallennetun avaamisen. Molemmista päädytään näkymään, jossa käyttäjä voi suorittaa navigaatiopalkissa esitettyjä toimintoja.

## Päätoiminnallisuudet

### Uusi tiedosto

Uuden tiedoston voi luoda aloitusnäkymästä. Avausnäkymään pääsee 'Tools' kohdan 'Show startup'-nappulasta.

![luo tiedosto](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/create_new_score.png?raw=true)

### Tiedoston tallennus, avaaminen ja poisto

Tiedoston voi tallentaa navigaatiopalkin 'Tools' kohdan alta löytyvästä 'Save score'-nappulasta. Score tallentuu nimen perusteella. Jos nimen vaihtaa jo olemassaolevaan nimeen ja tiedoston tallentaa, vanha tallennus ylikirjoitetaan. Muussa tapauksessa nimen muuttaminen luo uuden tiedoston tallennusvaiheessa.

![tallenna tiedosto](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/save_score.png?raw=true)

Tiedostoja voi avata ja poistaa avausnäkymän 'Saved scores'-nappulaa klikkaamalla. Avausnäkymään pääsee 'utils' kohdan 'Show startup'-nappulasta.

### Playback

Navigaatiopalkin 'play' ja 'stop' -nappulat soittavat ja keskeyttävät editoitavana olevan kappaleen. Äänet ovat tallennettuna wav-muotoisena, ja playback toimii ainakin macillä ja linuxilla (testattu virtuaalityöasemassa)

![playback](https://github.com/yuzamonkey/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/playback.png?raw=true)


## Tiedostojen tallentaminen ja tallennettujen tiedostojen avaaminen

Scoret tallennetaan luokkina käyttämällä pythonin pickle-moduulia score_repository-luokassa. Tiedostot tallentuvat projektin _data_/_scores_-hakemiston alle. Ohjelma hakee tiedostot editoitavaksi kyseisestä hakemistosta. Hakemisto _data_/_scores_ luodaan komennolla `poetry run invoke build`.