number_to_check = int(input("Podaj liczbę do sprawdzenia: "))

def number_is_even (number_to_check):
    return not bool(number_to_check % 2)

if number_is_even(number_to_check):
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")

