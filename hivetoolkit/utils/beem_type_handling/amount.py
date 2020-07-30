from beem.amount import Amount


def amount_to_dict(amount):  # TODO: inplement testing
    """return an amount in a dict form

    Args:
        amount (beem.amount.Amount): amount to transform  

    Raises:
        TypeError: wrong arg type  

    Returns:
        dict: {symbol: amount}
    """
    if not isinstance(amount, Amount):
        raise TypeError(f"amount argument must be an instance of Beem.amount.Amount")
    number, symbol = amount.tuple()
    return {symbol: number}
