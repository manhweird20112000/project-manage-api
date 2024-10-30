from pydantic import BaseModel, Field, field_validator
from app.core.validations.validators import is_not_empty, is_email

class LoginDto(BaseModel):
    email: str =  Field(...,max_length=64, description='メールlは50文字を超えています。')
    password: str = Field(...,max_length=64, description='パスワードは50文字を超えています。')

    @field_validator('email')
    def validate_email(cls, value):
        is_not_empty(value, 'メール')
        is_email(value, 'メール')
        return value

    @field_validator('password')
    def validate_password(cls, value):
        is_not_empty(value, 'パスワード')
        return value
