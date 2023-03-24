"""add foreign-key to post table

Revision ID: df475f97eb89
Revises: 8f8a8ac9ff7d
Create Date: 2023-03-23 21:20:54.747112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df475f97eb89'
down_revision = '8f8a8ac9ff7d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post', sa.Column('user_id', sa.Integer, nullable=False))
    op.create_foreign_key('post_user_fk', source_table='post', 
            referent_table='users', local_cols=['user_id'])
    pass


def downgrade() -> None:
    pass
