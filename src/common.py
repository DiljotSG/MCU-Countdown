from datetime import date


def is_valid_date(given_date: str):
    result = True
    try:
        str(date.fromisoformat(given_date))
        result = True
    except ValueError:
        result = False

    return result
