def filter_by_state(unsorted_list: list, state: str = "EXECUTED") -> list:
    """Сортировка по указанному ключу: state"""
    list_sort = []

    for x in unsorted_list:
        if x.get("state") == state:
            list_sort.append(x)
        # else:
        #     raise ValueError("Аргумент state, не найден в списке")
    return list_sort


def sort_by_date(unsorted_list: list, reverse: bool = True) -> list:
    """Сортировка по дате"""
    for data_correct in unsorted_list:
        if data_correct.get("date") == "":
            raise ValueError("Неверный формат")
        elif data_correct.get("date")[4] != "-":
            raise ValueError("Неверный формат")
        elif data_correct.get("date")[7] != "-":
            raise ValueError("Неверный формат")

    return sorted(unsorted_list, key=lambda x: x["date"], reverse=reverse)
