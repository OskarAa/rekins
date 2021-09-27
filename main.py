import rekins

def print_info():

    txt = ('\033[94m{}\033[0m'.format("[Rēķinu izrakstīšanas programma]"))
    INF = txt.center(65)
    print(INF)

def user_input():
    print("\033[94m{}\033[0m".format("[Programma, lai uzdotu pāris jautājumus un iestatītu galīgo rēķinu]"))

    name = input("Jusu vārds: ")
    text = input("Jūsu teksts: ")
    height = float(input("Cik augstu kaste vēlas? "))
    width = float(input("Cik platu kastīti vēlaties? (tikai veseli skaitļi): "))
    material = float(input("materiāla cena: "))
    length = float(input("Cik garumu kaste vēlas? "))

    darba_samaksa = 15
    PVN = 21

    produkta_cena = width/100.0 * length/100*height/100/3*material
    PVN_summa = produkta_cena + darba_samaksa * PVN / 100
    rekina_summa = produkta_cena + darba_samaksa + PVN_summa


    f = open("rekins.txt", "w")
    f.write("Datums: " + format(today))
    f.write("\n")
    f.write("Jusu vards: " + format(name))
    f.write("\n")
    f.write("Jusu teksts: " + format(text))
    f.write("\n")
    f.write("Produkta cena: " + format(produkta_cena, ",.2f"))
    f.write("\n")
    f.write("PVN summa: " + format(PVN_summa, ",.2f"))
    f.write("\n")
    f.write("Rekina summa: " + format(rekina_summa, ",.2f"))
    f.close()

    print("\033[94m{}\033[0m".format("--------------------------------"))
    print("Produkta cena: €" + format(produkta_cena, ",.2f"))
    print("PVN summa: €" + format(PVN_summa, ",.2f"))
    print("Rekina summa: €" + format(rekina_summa, ",.2f"))
    print("\033[94m{}\033[0m".format("--------------------------------"))


from datetime import date

today = date.today()
print("Šodienas datums:", "[", today , "]")

if __name__ == '__main__':
    print_info()
    while True:
       user_input()
       restart = input('Vai vēlaties izveidot jaunu? (Y/N) ').lower()
       if restart == "y":
           print_info()
       else:
           break
