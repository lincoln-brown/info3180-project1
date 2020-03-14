"""empty message

Revision ID: 13a72dd926c7
Revises: 
Create Date: 2020-03-14 00:33:27.028188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13a72dd926c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_profiles', 'biography',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('user_profiles', 'email',
               existing_type=sa.VARCHAR(length=225),
               nullable=True)
    op.alter_column('user_profiles', 'first_name',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('user_profiles', 'gender',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('user_profiles', 'last_name',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('user_profiles', 'location',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('user_profiles', 'photo',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.create_unique_constraint(None, 'user_profiles', ['gender'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_profiles', type_='unique')
    op.alter_column('user_profiles', 'photo',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('user_profiles', 'location',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('user_profiles', 'last_name',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('user_profiles', 'gender',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('user_profiles', 'first_name',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('user_profiles', 'email',
               existing_type=sa.VARCHAR(length=225),
               nullable=False)
    op.alter_column('user_profiles', 'biography',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###