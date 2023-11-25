"""nullable url

Revision ID: 75f0f3beb7fa
Revises: 70a87c0a844c
Create Date: 2023-11-24 17:04:10.167936

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75f0f3beb7fa'
down_revision: Union[str, None] = '70a87c0a844c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feeds', schema=None) as batch_op:
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feeds', schema=None) as batch_op:
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
