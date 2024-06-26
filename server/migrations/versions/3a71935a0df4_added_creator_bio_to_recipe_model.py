"""added creator_bio to Recipe model

Revision ID: 3a71935a0df4
Revises: 138c256e9d46
Create Date: 2024-05-22 14:31:32.167339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a71935a0df4'
down_revision = '138c256e9d46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('creator_bio', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('recipe_memory', sa.Text(), nullable=True))
        batch_op.drop_column('creator_memory')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('creator_memory', sa.TEXT(), nullable=True))
        batch_op.drop_column('recipe_memory')
        batch_op.drop_column('creator_bio')

    # ### end Alembic commands ###
