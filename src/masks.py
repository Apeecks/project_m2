def get_mask_card_number(x: str) -> str:
    """Маскировка номера банковской карты"""
    return x[0:4] + " " + x[4:6] + "**" + " " + "****" + " " + x[12:16]


def get_mask_account(account: str) -> str:
    """Маскировка номера банковского счета"""
    return account.replace(account[:16], "**")


# x = "1234123412341234"
x = "1111111111111111"
print(get_mask_card_number(x))