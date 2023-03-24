"""Create post table

Revision ID: 6e12055116dc
Revises: 
Create Date: 2023-03-23 19:21:09.749787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e12055116dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('post', sa.)
    pass


def downgrade() -> None:
    pass
