"""add foreign key to post table

Revision ID: 01ff1508bdf9
Revises: 080816530688
Create Date: 2022-02-27 16:10:49.597551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01ff1508bdf9'
down_revision = '080816530688'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
