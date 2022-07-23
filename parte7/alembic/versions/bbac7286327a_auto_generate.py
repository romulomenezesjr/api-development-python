"""Auto generate

Revision ID: bbac7286327a
Revises: 7c815a3def16
Create Date: 2022-07-18 18:40:35.255941

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bbac7286327a'
down_revision = '7c815a3def16'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('role', sa.String(length=255), server_default='user', nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('contents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('playlist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlists.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contents_id'), 'contents', ['id'], unique=False)
    op.create_table('liked_playlists',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('playlist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlists.id'], onupdate='cascade', ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('user_id', 'playlist_id')
    )
    op.create_table('user_like_playlist',
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('playlist', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['playlist'], ['playlists.id'], ),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user', 'playlist')
    )
    op.drop_table('posts')
    op.add_column('playlists', sa.Column('title', sa.String(length=255), nullable=True))
    op.add_column('playlists', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('playlists', sa.Column('thumbnail', sa.String(length=255), nullable=True))
    op.add_column('playlists', sa.Column('favcount', sa.Integer(), server_default='0', nullable=False))
    op.add_column('playlists', sa.Column('published', sa.Boolean(), server_default='1', nullable=False))
    op.add_column('playlists', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('playlists', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_playlists_id'), 'playlists', ['id'], unique=False)
    op.create_foreign_key(None, 'playlists', 'users', ['owner_id'], ['id'], onupdate='cascade', ondelete='cascade')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'playlists', type_='foreignkey')
    op.drop_index(op.f('ix_playlists_id'), table_name='playlists')
    op.drop_column('playlists', 'owner_id')
    op.drop_column('playlists', 'created_at')
    op.drop_column('playlists', 'published')
    op.drop_column('playlists', 'favcount')
    op.drop_column('playlists', 'thumbnail')
    op.drop_column('playlists', 'description')
    op.drop_column('playlists', 'title')
    op.create_table('posts',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('content', mysql.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('user_like_playlist')
    op.drop_table('liked_playlists')
    op.drop_index(op.f('ix_contents_id'), table_name='contents')
    op.drop_table('contents')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
