def get_mask_card_number(cart_namber: str) -> str:
    """Маскировка номера банковской карты"""
    mask_cart_number = []
    x = cart_namber.replace(cart_namber[6:12], "******")
    mask_cart_number.append(x[0:4])
    mask_cart_number.append(x[4:8])
    mask_cart_number.append(x[8:12])
    mask_cart_number.append(x[12:16])
    return " ".join(mask_cart_number)


def get_mask_account(account: str) -> str:
    """Маскировка номера банковского счета"""
    # mask_account = account.replace(account[:12], "**")
    return account.replace(account[:16], "**")
