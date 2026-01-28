from datetime import date


def is_valid_date(given_date: str) -> bool:
    try:
        date.fromisoformat(given_date)
        return True
    except (ValueError, TypeError):
        return False
