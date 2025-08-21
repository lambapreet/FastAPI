"""add column 

Revision ID: 3972ae63280c
Revises: 32f39c3e8d2a
Create Date: 2025-08-21 10:57:48.005543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3972ae63280c'
down_revision: Union[str, Sequence[str], None] = '32f39c3e8d2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone", sa.Integer()))


def downgrade() -> None:
    op.drop_column("users","phone")
