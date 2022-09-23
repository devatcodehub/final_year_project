"""empty message

Revision ID: 12fac9c521d0
Revises: 1c87851a105d
Create Date: 2022-09-22 17:00:54.875465

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '12fac9c521d0'
down_revision = '1c87851a105d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.drop_table('follows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('follower_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('followed_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], name='follows_followed_id_fkey'),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], name='follows_follower_id_fkey'),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id', name='follows_pkey')
    )
    op.drop_table('followers')
    # ### end Alembic commands ###
