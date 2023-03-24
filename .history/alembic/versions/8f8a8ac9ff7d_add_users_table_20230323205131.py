"""add users table

Revision ID: 8f8a8ac9ff7d
Revises: 708598d0bb15
Create Date: 2023-03-23 20:49:07.438735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f8a8ac9ff7d'
down_revision = '708598d0bb15'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer, primary_key=True, nullable=False),
                            sa.Column('email', sa.String, nullable=False))
    pass


def downgrade() -> None:
    pass
