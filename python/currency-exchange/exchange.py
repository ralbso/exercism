def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return float(budget / exchange_rate)


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return float(budget - exchanging_value)


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return float(denomination * number_of_bills)


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return float(budget // denomination)


def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    number_of_bills = get_number_of_bills(budget, denomination)
    return float(budget - (number_of_bills * denomination))


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread = spread / 100
    exchange_rate = exchange_rate + (exchange_rate * spread)
    exchanged_money = exchange_money(budget, exchange_rate)

    return int(get_number_of_bills(exchanged_money, denomination) * denomination)

if __name__ == "__main__":
    print(exchangeable_value(100000, 10.61, 10, 1))
    print(exchangeable_value(1500, 0.84, 25, 40))
    print(exchangeable_value(470000, 1050, 30, 10000000000))
    print(exchangeable_value(470000, 0.00000009, 30, 700))
    print(exchangeable_value(425.33, 0.0009, 30, 700))
