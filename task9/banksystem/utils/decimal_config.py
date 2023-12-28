from decimal import Decimal


def convert_to_decimal(value):
    allowed_types = (int, str, float, Decimal)

    if not isinstance(value, allowed_types):
        raise TypeError(
            "Неверный тип данных. Поддерживаемые типы: int, str, float, Decimal."
        )

    return Decimal(str(value))
