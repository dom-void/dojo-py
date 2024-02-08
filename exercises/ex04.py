number_to_check = int(input("Podaj liczbę do sprawdzenia: "))

def is_prime(number_to_check):
    i = 2
    while i < number_to_check:
        if number_to_check % i == 0:
            return False
        i += 1
    return True

# def sum_digits (number):
#     digits_string = str(number)
#     digits_sum = 0
#     for digit in digits_string:
#         digits_sum = digits_sum + int(digit)
#     return digits_sum

def sum_digits (number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = (number - (number % 10)) / 10
    return sum

def is_super_prime (number_to_check):
    digits_sum = sum_digits(number_to_check)
    if is_prime(digits_sum) and is_prime(number_to_check):
        return True
    else:
        return False

def sum_binary_is_prime (number):
    sum = sum_digits(number)
    acc = 0
    while sum > 0:
        acc += sum % 2
        sum = int(sum / 2)
    return is_prime(acc)

if is_super_prime(number_to_check):
    if sum_binary_is_prime(number_to_check):
        print("Liczba jest B super pierwsza!")
    else:
        print("Liczba jest super pierwsza, ale nie B super pierwsza")
else:
    print("Liczba nie jest super pierwsza")
    
