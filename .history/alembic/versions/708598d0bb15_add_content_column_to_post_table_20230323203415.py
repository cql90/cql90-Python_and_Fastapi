"""add content column to post table

Revision ID: 708598d0bb15
Revises: 6e12055116dc
Create Date: 2023-03-23 20:32:12.960911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '708598d0bb15'
down_revision = '6e12055116dc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    pass
 