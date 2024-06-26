"""Add creator information to Recipe model

Revision ID: b976062218fd
Revises: 
Create Date: 2024-05-21 21:01:12.371283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b976062218fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('creator_first_name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('creator_last_name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('creator_nickname', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('creator_birth_year', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('creator_death_year', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('creator_memory', sa.Text(), nullable=True))
        batch_op.drop_column('creator_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('creator_name', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('creator_memory')
        batch_op.drop_column('creator_death_year')
        batch_op.drop_column('creator_birth_year')
        batch_op.drop_column('creator_nickname')
        batch_op.drop_column('creator_last_name')
        batch_op.drop_column('creator_first_name')

    # ### end Alembic commands ###
