"""Updated Thread Model to include a value for the thread

Revision ID: c7e8beb3ce4d
Revises: b30a2ffe60e8
Create Date: 2023-11-13 17:12:44.120113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7e8beb3ce4d'
down_revision = 'b30a2ffe60e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('thread', schema=None) as batch_op:
        batch_op.add_column(sa.Column('value', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('thread', schema=None) as batch_op:
        batch_op.drop_column('value')

    # ### end Alembic commands ###
