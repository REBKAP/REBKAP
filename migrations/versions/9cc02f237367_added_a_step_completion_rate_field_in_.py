"""added a step_completion_rate field in Projects to track step completions.

Revision ID: 9cc02f237367
Revises: a47d775aca5b
Create Date: 2024-02-06 22:15:29.425511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cc02f237367'
down_revision = 'a47d775aca5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('step_completion_rate', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_column('step_completion_rate')

    # ### end Alembic commands ###
