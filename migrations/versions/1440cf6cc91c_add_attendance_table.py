""" Add attendance table

Revision ID: 1440cf6cc91c
Revises: 532c3f11a51b
Create Date: 2015-07-23 14:25:31.499110

"""

# revision identifiers, used by Alembic.
revision = '1440cf6cc91c'
down_revision = '532c3f11a51b'

from alembic import op
import sqlalchemy as sa
from models import JsonType


def upgrade():
    op.create_table(
        'attendance',
        sa.Column('organization_url', sa.Unicode(), nullable=False),
        sa.Column('total', sa.Integer(), nullable=True),
        sa.Column('weekly', JsonType, nullable=True),
        sa.Column('organization_name', sa.Unicode(), nullable=False),
        sa.ForeignKeyConstraint(['organization_name'], ['organization.name'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('organization_url')
    )

def downgrade():
    op.drop_table('attendance')
