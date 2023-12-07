try:
    print("Tere! Olen sinu uus sõber - Python!")
    nimi = str(input("Sinu nimi on: "))
    print(nimi + ", oi kui ilus nimi!")
    print(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>")

    vastus = int(input())

    if vastus == 1:
        pikkus = int(input("Sinu pikkus on: "))
        mass = float(input("Sinu mass on: "))
        indeks = (mass / (0.01 * pikkus) ** 2)

        print(nimi + "! Sinu keha indeks on: " + str(round(indeks, 2)))

        if indeks < 16:
            print("Tervisele ohtlik alakaal")
        elif 16 <= indeks < 19:
            print("Alakaal")
        elif 19 <= indeks < 25:
            print("Normaalkaal")
        elif 25 <= indeks < 30:
            print("Ulekaal")
        elif 30 <= indeks < 35:
            print("Rasvumine")
        elif 35 <= indeks < 40:
            print("Tugev rasvumine")
        elif indeks >= 40:
            print("Tervisele ohtlik rasvumine")
    else:
        print("Kahju! See on väga kasulik info!")
        print()
        print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

except ValueError:
    print("Error")


