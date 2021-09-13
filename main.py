import rekins

def print_info():
    print('programma rekina sagatavosana')


def lietotaja_ievads():
    vards = input('Ieraksti savu vardu:')
    teksts = input('Ieraksti savu tekstu:')
    kokmateriala_cena = input('Kokmateriala cena')
    platums = input('Cik platu kastisti velies?: (Tikai veselie skaitli)')
    garums = input('Cik izmers? Garums: (mm)')
    augstums = input('Cik izmers? Augstums: (mm)')

    return vards, teksts, platums, garums, augstums, kokmateriala_cena


if __name__ == '__main__':
    print_info()
    while 1>0:
        lietotaja_ievads()
        rekins = rekins.Rekins()
        run_again = input("Vai velies sagatavot reikinu velreiz?", ja = 1, ne = 0)
