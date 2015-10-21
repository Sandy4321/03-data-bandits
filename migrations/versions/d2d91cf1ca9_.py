"""empty message

Revision ID: d2d91cf1ca9
Revises: None
Create Date: 2015-10-20 21:24:42.398717

"""

# revision identifiers, used by Alembic.
revision = 'd2d91cf1ca9'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('componentIncome',
    sa.Column('component', sa.String(length=80), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('all_units', sa.Integer(), nullable=True),
    sa.Column('less_than_five', sa.Integer(), nullable=True),
    sa.Column('five_to_ten', sa.Integer(), nullable=True),
    sa.Column('ten_to_fifteen', sa.Integer(), nullable=True),
    sa.Column('fifteen_to_twenty', sa.Integer(), nullable=True),
    sa.Column('twenty_to_thirty', sa.Integer(), nullable=True),
    sa.Column('thirty_to_fourty', sa.Integer(), nullable=True),
    sa.Column('fourty_to_fifty', sa.Integer(), nullable=True),
    sa.Column('fifty_to_seventy', sa.Integer(), nullable=True),
    sa.Column('seventy_or_more', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('component', 'year')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('componentIncome')
    ### end Alembic commands ###