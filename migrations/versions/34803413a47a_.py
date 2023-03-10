"""empty message

Revision ID: 34803413a47a
Revises: 981135a1395a
Create Date: 2023-01-30 16:03:56.266007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34803413a47a'
down_revision = '981135a1395a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), server_default=sa.text("'1'"), nullable=True))
        batch_op.create_foreign_key('fk_user_user_id_user', 'user', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    # ### end Alembic commands ###
