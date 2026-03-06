"""create companies table

Revision ID: 001
Revises:
Create Date: 2026-03-06

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "companies",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("street", sa.String(255), nullable=False),
        sa.Column("city", sa.String(100), nullable=False),
        sa.Column("state", sa.String(100), nullable=False),
        sa.Column("zip_code", sa.String(20), nullable=False),
        sa.Column("country", sa.String(100), nullable=False),
        sa.Column("billing", sa.Numeric(12, 2), nullable=False, server_default="0"),
        sa.Column("expenses", sa.Numeric(12, 2), nullable=False, server_default="0"),
        sa.Column("employees", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("clients", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("companies")
