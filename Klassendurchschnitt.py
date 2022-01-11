x = float((input("Was ist der Klassendurchschnitt: ")))

Schüler = int(input("Wie viele Kinder sind sie in der Klasse: "))

Note1 = float(input("Welche Note wollen sie weglassen: "))

Frage = str((input("Wollen sie noch eine Note weglassen: ")))

Note2 = float(input("Welche Note wollen sie weglassen: "))



if Frage == "ja":

    print(((x * Schüler) - (Note1 + Note2)) / (Schüler - 2))

else:

    print(x * Schüler - Note1 / Schüler - 1)
