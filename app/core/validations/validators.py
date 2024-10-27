import re
from pydantic import ValidationError

def is_not_empty(val: str, field: str):
    if not val.strip():
        raise ValueError(f'{field}は必須です。',)
    return val.strip()


def is_email(val: str, field: str):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if val and not re.match(pattern, val):
        raise ValueError('メールアドレスの形式が正しくありません。')

    return val

