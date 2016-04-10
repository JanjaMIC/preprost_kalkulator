st_1 = float(raw_input("Izberi prvo stevilo: "))
st_2 = float(raw_input("Izberi drugo stevilo: "))

operacija = (raw_input("Izberi operacijo: deljenje, mnozenje, sestevanje, odstevanje:").lower())

print "Racunalnik bo sedaj izvedel operacijo, ki ste jo izbrali za izbrani stevilki. Pricenja se... " + operacija + "!"

def racunalo(st_1, st_2):
    if operacija == "deljenje":
        print "Rezultat je naslednji", st_1 / st_2

    elif operacija == "mnozenje":
        print "Rezultat je naslednji:", st_1 * st_2

    elif operacija == "sestevanje":
        print "Rezultat je naslednji: ", st_1 + st_2

    elif operacija == "odstevanje":
        print "Rezultat je naslednji: ", st_1 - st_2
        return racunalo(st_1, st_2)

print racunalo(st_1, st_2)