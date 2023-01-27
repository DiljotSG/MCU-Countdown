from datetime import date

import jsonschema


def is_valid_schema(obj, schema: dict) -> bool:
    result = True
    try:
        jsonschema.validate(instance=obj, schema=schema)
    except jsonschema.ValidationError:
        result = False
    return result


def is_valid_date(given_date: str):
    result = True
    try:
        str(date.fromisoformat(given_date))
        result = True
    except ValueError:
        result = False

    return result
