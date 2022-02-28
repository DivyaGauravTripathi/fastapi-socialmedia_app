"""add content column to post table

Revision ID: 23a783ff26d2
Revises: daed6fba9a30
Create Date: 2022-02-27 15:55:21.702791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23a783ff26d2'
down_revision = 'daed6fba9a30'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
