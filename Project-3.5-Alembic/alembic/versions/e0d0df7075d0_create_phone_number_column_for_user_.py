"""create phone number column for user table

Revision ID: e0d0df7075d0
Revises: 
Create Date: 2026-10-21 16:26:20.609838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0d0df7075d0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # pass
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))

def downgrade() -> None:
    """Downgrade schema."""
    pass
    # op.drop_column('users', 'phone_number')