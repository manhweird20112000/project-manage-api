from typing import Any


def format_validation_errors(fields: dict[str, Any]) -> dict[str, str]:
    errors : dict[str, str] = {}

    for field in fields:
        errors[field['loc'][1]] = str(field['msg']).replace('Value error, ', '')

    return errors