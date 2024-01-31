import os
import lyricsgenius

genius = lyricsgenius.Genius(os.getenv('GENIUS_TOKEN'), verbose=True)

print('Ez a priogranm kiírja egy általad megadott zenész pár művét,'
      ' abból te választhatsz egyet és a program kiírja a szövegét', end='\n')
eloado = input('Adj meg egy zenészt: ')


def dalok_keresese():
    dalok = genius.search_songs(eloado)
    szamok = len(dalok['hits'])

    albumok = []
    for x in range(szamok):
        print(dalok['hits'][x]['result']['title'])
        albumok.append(dalok['hits'][x]['result']['title'])

    return albumok


def dont(album, valasztott):
    if valasztott in album:
        szoveg = genius.search_song(valasztott, eloado, get_full_info=True)
        print(f'A dal szövege: ', '\n', szoveg.to_dict()['lyrics'])

    else:
        print(':( Ez nincs is benne a választható számok között, válassz másikat')
        dont(dalok_keresese(), valaszt())


def valaszt():
    valasztas = input('Add meg a választott dalt: ')
    return valasztas


def main():
    dont(dalok_keresese(), valaszt())


main()
