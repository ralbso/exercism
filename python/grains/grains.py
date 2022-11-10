def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        result = 2 ** (number - 1)
    return result

def total():
    return 2 * square(64) - 1


if __name__ == "__main__":
    print(total())
