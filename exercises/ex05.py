def number_is_perfect (number_to_check):
    divider = 1
    acc = 0
    while divider < number_to_check:
        if not number_to_check % divider:
            acc += divider
        divider += 1
    return number_to_check == acc

number_to_check = int(input("Podaj liczbę do sprawdzenia: "))

if number_is_perfect(number_to_check):
    print("Liczba", number_to_check, "jest perfekcyjna!")
else:
    print("Liczba", number_to_check, "nie jest perfekcyjna!")
