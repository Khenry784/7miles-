"""empty message

Revision ID: 8fd2eb9f218f
Revises: 292addf1bded
Create Date: 2021-03-12 14:56:30.230231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fd2eb9f218f'
down_revision = '292addf1bded'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('quantity', sa.Integer(), nullable=True))
    op.add_column('user_profiles', sa.Column('email', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'email')
    op.drop_column('items', 'quantity')
    # ### end Alembic commands ###