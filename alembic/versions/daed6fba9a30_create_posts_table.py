"""create posts table

Revision ID: daed6fba9a30
Revises: 
Create Date: 2022-02-27 15:31:51.452365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daed6fba9a30'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
    sa.Column('title',sa.String(),nullable=False))
    pass

def downgrade():
    op.drop_table('posts')
    pass