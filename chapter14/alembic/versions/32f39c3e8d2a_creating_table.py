"""creating table

Revision ID: 32f39c3e8d2a
Revises: 
Create Date: 2025-08-21 10:34:51.365775

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32f39c3e8d2a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id",sa.INTEGER, primary_key=True),
        sa.Column("name",sa.VARCHAR(50),nullable=False),
        sa.Column("email",sa.String),
    )

def downgrade() -> None:
    op.drop_table('users')