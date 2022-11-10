def is_armstrong_number(number):
    n_digits = len(str(number))
    digits = list(str(number))

    result = 0
    for digit in digits:
        result += int(digit) ** n_digits

    if result == number:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_armstrong_number(153))