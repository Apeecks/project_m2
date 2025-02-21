from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "cart_namber, result, error_cart_namber, error_result",
    [
        ("1111111111111111", "1111 11** **** 1111", "111111111111111111", "Неправильно введен номер карты"),
        ("1111222233334444", "1111 22** **** 4444", "11112222333344", "Неправильно введен номер карты"),
        ("1234567890123456", "1234 56** **** 3456", "", "Номер карты не введен"),
    ],
)
def test_get_mask_card_number(cart_namber: str, result: str, error_cart_namber: str, error_result: str) -> Any:
    """Проверка функции get_mask_card_number"""
    assert get_mask_card_number(cart_namber) == result
    with pytest.raises(TypeError) as file:
        get_mask_card_number(error_cart_namber)
    assert str(file.value) == error_result


@pytest.mark.parametrize(
    "account, result, error_account, error_result",
    [
        ("11111111111111111111", "**1111", "1111111111111111111111", "Неправильно введен номер счета"),
        ("11112222333344445555", "**5555", "111122223333444455", "Неправильно введен номер счета"),
        ("12345678901234567890", "**7890", "", "Номер счета не введен"),
    ],
)
def test_get_mask_account(account: str, result: str, error_account: str, error_result: str) -> Any:
    """Проверка функции get_mask_account"""
    assert get_mask_account(account) == result
    with pytest.raises(TypeError) as file:
        get_mask_account(error_account)
    assert str(file.value) == error_result
