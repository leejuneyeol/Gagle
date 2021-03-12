"""empty message

Revision ID: 2203a8b26c3f
Revises: 40f7db4f22e2
Create Date: 2021-03-09 22:14:46.806560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2203a8b26c3f'
down_revision = '40f7db4f22e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###