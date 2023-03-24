"""add more column to post table

Revision ID: 4951d60ef2df
Revises: df475f97eb89
Create Date: 2023-03-23 21:39:00.099679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4951d60ef2df'
down_revision = 'df475f97eb89'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post',  sa.Column('published', sa.Boolean(), nullable=True, server_default=True))
    op.add_column('post', sa.Column('create_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    pass
