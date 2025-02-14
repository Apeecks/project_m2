def get_mask_card_number(cart_namber: str) -> str:
    """Маскировка номера банковской карты"""
    if cart_namber == "":
        raise TypeError("Номер карты не введен")
    elif len(cart_namber) != 16:
        raise TypeError("Неправильно введен номер карты")

    return cart_namber[0:4] + " " + cart_namber[4:6] + "**" + " " + "****" + " " + cart_namber[12:16]


def get_mask_account(account: str) -> str:
    """Маскировка номера банковского счета"""
    if account == "":
        raise TypeError("Номер счета не введен")
    elif len(account) != 20:
        raise TypeError("Неправильно введен номер счета")

    return account.replace(account[:16], "**")
