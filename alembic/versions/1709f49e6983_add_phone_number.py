"""add phone number

Revision ID: 1709f49e6983
Revises: 5ae35edf8ff1
Create Date: 2022-02-27 19:27:56.611210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1709f49e6983'
down_revision = '5ae35edf8ff1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
