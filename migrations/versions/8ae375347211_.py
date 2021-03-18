"""empty message

Revision ID: 8ae375347211
Revises: 845bd3f6dd60
Create Date: 2021-03-12 10:24:01.753191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ae375347211'
down_revision = '845bd3f6dd60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('photo', sa.String(length=80), nullable=True))
    op.drop_column('items', 'photo_filename')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('photo_filename', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.drop_column('items', 'photo')
    # ### end Alembic commands ###