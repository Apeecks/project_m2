from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "cart_namber, result",
    [
        ("1111111111111111", "1111 11** **** 1111"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("1234567890123456", "1234 56** **** 3456"),
    ]
)
def test_get_mask_card_number(cart_namber: str, result: str) -> Any:
    """Проверка функции get_mask_card_number"""
    assert get_mask_card_number(cart_namber) == result


@pytest.mark.parametrize(
    "cart_namber, result",
    [
        ("111111111111111111", "Неправильно введен номер карты"),
        ("11112222333344", "Неправильно введен номер карты"),
        ("", "Номер карты не введен")
    ]
)
def test_error_get_mask_card_number(cart_namber: str, result: str) -> Any:
    """Проверка функции get_mask_card_number на ошибки"""
    with pytest.raises(TypeError) as file:
        get_mask_card_number(cart_namber)
    assert str(file.value) == result


@pytest.mark.parametrize(
    "account, result",
    [
        ("11111111111111111111", "**1111"),
        ("11112222333344445555", "**5555"),
        ("12345678901234567890", "**7890")
    ]
)
def test_get_mask_account(account: str, result: str) -> Any:
    """Проверка функции get_mask_account"""
    assert get_mask_account(account) == result


@pytest.mark.parametrize(
    "account, result",
    [
        ("1111111111111111111111", "Неправильно введен номер счета"),
        ("111122223333444455", "Неправильно введен номер счета"),
        ("", "Номер счета не введен")
    ]
)
def test_error_get_mask_account(account: str, result: str) -> Any:
    """Проверка функции get_mask_account на ошибки"""
    with pytest.raises(TypeError) as file:
        get_mask_account(account)
    assert str(file.value) == result
