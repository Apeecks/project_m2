def filter_by_state(list_: list, state="EXECUTED") -> list:
    """Сортировка по указанному ключу: state"""
    list_sort = []
    for x in list_:
        if x.get("state") == state:
            list_sort.append(x)
        else:
            continue
    return list_sort


def sort_by_date(list_, a=True):
    """Сортировка по дате"""
    return sorted(list_, key=lambda x: x['date'], reverse=a)
