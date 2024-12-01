"""add attachment_type

Revision ID: 468eb3c021be
Revises: c907aa22355f
Create Date: 2024-12-01 17:55:10.203112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '468eb3c021be'
down_revision: Union[str, None] = 'c907aa22355f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('attachment_type', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'attachment_type')
    # ### end Alembic commands ###
