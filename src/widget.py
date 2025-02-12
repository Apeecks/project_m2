import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_cart: str) -> str:
    """Получение, сведений о карте или счете"""
    number = "".join(re.findall(r"[0-9]", info_cart))

    if number == "":
        raise TypeError("Неверный формат")
    elif len(number) != 16:
        if len(number) != 20:
            raise TypeError("Неверный формат")

    if len(number) == 16:
        numser_masks = get_mask_card_number(number)
        info_cart_masks = info_cart.replace(info_cart[-16:], numser_masks)
    else:
        numser_masks = get_mask_account(number)
        info_cart_masks = info_cart.replace(info_cart[-20:], numser_masks)
    return info_cart_masks


def get_date(data: str) -> str:
    """ Изменение формата даты """
    if data == "":
        raise ValueError("Неверный формат")
    elif data[4] != "-":
        raise ValueError("Неверный формат")
    elif data[7] != "-":
        raise ValueError("Неверный формат")

    data_t = [data[8:10], data[5:7], data[0:4]]

    return ".".join(data_t)
