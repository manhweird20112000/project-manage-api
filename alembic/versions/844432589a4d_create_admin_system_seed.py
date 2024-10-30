"""create admin system seed

Revision ID: 844432589a4d
Revises: 176fbc69cf08
Create Date: 2024-10-27 14:41:11.924230

"""
from typing import Sequence, Union

import bcrypt
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import Admin
from app.models.admin import ERole

# revision identifiers, used by Alembic.
revision: str = '844432589a4d'
down_revision: Union[str, None] = '176fbc69cf08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    salt = bcrypt.gensalt()
    # Hashing the password
    hashed = bcrypt.hashpw(b'123456xX', salt)

    data = [
        Admin(
            name='Admin System',
            status=1,
            role= ERole.system,
            password=str(hashed.decode('utf-8')),
            email='admin@domain.com'
        )
    ]

    session.bulk_save_objects(data)
    session.commit()
    pass


def downgrade() -> None:
    pass
