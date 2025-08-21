"""upgrade column 

Revision ID: 2e5c6c207553
Revises: 3972ae63280c
Create Date: 2025-08-21 11:10:22.910585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e5c6c207553'
down_revision: Union[str, Sequence[str], None] = '3972ae63280c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.create_unique_constraint("uq_phone_number", ["phone"])

def downgrade():
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_constraint("uq_phone_number", type_="unique")
