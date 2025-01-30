import re
from masks import get_mask_card_number, get_mask_account

def mask_account_card(info_cart: str) -> str:
    """ Получение, сведений о карте или счете """
    number = "".join(re.findall(r"[0-9]", info_cart))
    if len(number) == 16:
        numser_masks = get_mask_card_number(number)
        info_cart_masks = info_cart.replace(info_cart[-16:], numser_masks)
    else:
        numser_masks = get_mask_account(number)
        info_cart_masks = info_cart.replace(info_cart[-20:], numser_masks)
    return info_cart_masks


def get_date(data):
    data_t = [data[8:10], data[5:7], data[0:4]]
    return ".".join(data_t)