"""third

Revision ID: 3fbaedfce729
Revises: 6a2b70abac3e
Create Date: 2024-05-22 09:53:24.280548

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fbaedfce729'
down_revision: Union[str, None] = '6a2b70abac3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
