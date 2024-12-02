"""add text in tasks

Revision ID: 876f6ff5d6fa
Revises: 468eb3c021be
Create Date: 2024-12-01 21:12:17.918399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '876f6ff5d6fa'
down_revision: Union[str, None] = '468eb3c021be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('text', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'text')
    # ### end Alembic commands ###
