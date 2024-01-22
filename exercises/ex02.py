number_to_check = int(input("Podaj liczbę do sprawdzenia: "))

def is_prime(number_to_check):
    i = 2
    while i < number_to_check:
        if number_to_check % i == 0:
            return False
        i += 1
    return True

if is_prime(number_to_check):
    print("To jest liczba pierwsza!")
else:
    print("To nie jest liczba pierwsza.")

