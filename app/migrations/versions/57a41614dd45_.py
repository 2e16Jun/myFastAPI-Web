"""empty message

Revision ID: 57a41614dd45
Revises: 8740f2d5cbbf
Create Date: 2023-03-09 16:56:22.773376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57a41614dd45'
down_revision = '8740f2d5cbbf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('check', sa.Integer(), nullable=True,default =0))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('check')

    # ### end Alembic commands ###
