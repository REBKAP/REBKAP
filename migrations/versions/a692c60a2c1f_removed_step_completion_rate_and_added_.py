"""removed step_completion_rate and added most_completed_step and most_completed_step_id.

Revision ID: a692c60a2c1f
Revises: 9cc02f237367
Create Date: 2024-02-07 13:57:42.043055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a692c60a2c1f'
down_revision = '9cc02f237367'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('most_current_step_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('most_current_step', sa.String(length=150), nullable=True))
        batch_op.drop_column('step_completion_rate')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('step_completion_rate', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('most_current_step')
        batch_op.drop_column('most_current_step_id')

    # ### end Alembic commands ###
