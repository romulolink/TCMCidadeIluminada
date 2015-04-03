"""status

Revision ID: 420a26e3a847
Revises: 4e0939a0177a
Create Date: 2015-02-16 16:29:16.432711

"""

# revision identifiers, used by Alembic.
revision = '420a26e3a847'
down_revision = '4e0939a0177a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('protocolo', sa.Column('status', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('protocolo', 'status')
    ### end Alembic commands ###