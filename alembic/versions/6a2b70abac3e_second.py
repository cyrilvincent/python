"""second

Revision ID: 6a2b70abac3e
Revises: aa42007d5999
Create Date: 2024-05-22 09:51:03.108880

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a2b70abac3e'
down_revision: Union[str, None] = 'aa42007d5999'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
