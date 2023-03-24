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
    op.create_table('users', sa.Column('id', sa.Integer, nullable=False),
                            sa.Column('email', sa.String, nullable=False),
                            sa.Column('password', sa.String, nullable=False),
                            sa.Column('create_at', sa.TIMESTAMP(timezone=True), 
                                      server_default=sa.text('now()'), nullable=False),
                            sa.PrimaryKeyConstraint(id),
                            sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    sa.drop_table('users')
    pass
