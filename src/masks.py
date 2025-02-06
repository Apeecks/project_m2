def get_mask_card_number(cart_namber: str) -> str:
    """Маскировка номера банковской карты"""
    return x[0:4] + " " + x[4:6] + "**" + " " + "****" + " " + x[12:16]



def get_mask_account(account: str) -> str:
    """Маскировка номера банковского счета"""
    # mask_account = account.replace(account[:12], "**")
    return account.replace(account[:16], "**")
