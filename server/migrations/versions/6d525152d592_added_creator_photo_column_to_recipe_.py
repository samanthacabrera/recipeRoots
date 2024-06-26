"""added creator_photo column to Recipe model

Revision ID: 6d525152d592
Revises: 9b1543fe9991
Create Date: 2024-05-21 21:20:48.681444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d525152d592'
down_revision = '9b1543fe9991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('creator_photo', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.drop_column('creator_photo')

    # ### end Alembic commands ###
