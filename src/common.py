from jsonschema import validate
from jsonschema import ValidationError


def is_valid_schema(obj, schema: dict) -> bool:
    result = True
    try:
        validate(instance=obj, schema=schema)
    except ValidationError:
        result = False
    return result
