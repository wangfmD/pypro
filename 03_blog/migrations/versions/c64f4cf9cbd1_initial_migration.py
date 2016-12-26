"""initial migration

Revision ID: c64f4cf9cbd1
Revises: None
Create Date: 2016-08-15 16:03:34.745000

"""

# revision identifiers, used by Alembic.
revision = 'c64f4cf9cbd1'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('gst_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('gst_user', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('gst_title', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('gst_content', mysql.TEXT(), nullable=True),
    sa.Column('gst_time', mysql.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('gst_ip', mysql.VARCHAR(length=15), nullable=False),
    sa.PrimaryKeyConstraint('gst_id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    ### end Alembic commands ###
