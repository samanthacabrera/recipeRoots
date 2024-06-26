"""updated Favorite model

Revision ID: 730209817410
Revises: 641fdc0cca08
Create Date: 2024-05-23 13:48:15.791543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '730209817410'
down_revision = '641fdc0cca08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint('fk_favorites_recipe_id_recipes', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_favorites_recipe_id_recipes'), 'recipes', ['recipe_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_favorites_recipe_id_recipes'), type_='foreignkey')
        batch_op.create_foreign_key('fk_favorites_recipe_id_recipes', 'recipes', ['recipe_id'], ['id'])

    # ### end Alembic commands ###
