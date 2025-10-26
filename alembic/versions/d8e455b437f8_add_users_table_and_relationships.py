"""Add users table and relationships

Revision ID: d8e455b437f8
Revises: 2b6569552419
Create Date: 2025-10-25 21:01:39.207349

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8e455b437f8'
down_revision: Union[str, Sequence[str], None] = '2b6569552419'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # --- Users table ---
    op.create_table(
        'users',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('username', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=True)

    # --- Comments table ---
    op.add_column('comments', sa.Column('user_id', sa.UUID(), nullable=False))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('comments', 'author_id')

    # --- Likes table ---
    # Change VARCHAR -> UUID safely with explicit USING clause
    op.execute("ALTER TABLE likes ALTER COLUMN user_id TYPE UUID USING user_id::uuid;")
    op.create_foreign_key(None, 'likes', 'users', ['user_id'], ['id'], ondelete='CASCADE')

    # --- Posts table ---
    # Change VARCHAR -> UUID safely with explicit USING clause
    op.execute("ALTER TABLE posts ALTER COLUMN author_id TYPE UUID USING author_id::uuid;")
    op.create_foreign_key(None, 'posts', 'users', ['author_id'], ['id'], ondelete='CASCADE')


def downgrade() -> None:
    """Downgrade schema."""
    # --- Posts table ---
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.alter_column('posts', 'author_id',
               existing_type=sa.UUID(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    # --- Likes table ---
    op.drop_constraint(None, 'likes', type_='foreignkey')
    op.alter_column('likes', 'user_id',
               existing_type=sa.UUID(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    # --- Comments table ---
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.add_column('comments', sa.Column('author_id', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.drop_column('comments', 'user_id')

    # --- Users table ---
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
