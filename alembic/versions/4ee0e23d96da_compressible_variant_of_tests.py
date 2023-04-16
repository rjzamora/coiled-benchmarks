"""compressible variant of tests

Revision ID: 4ee0e23d96da
Revises: 2381a77e8487
Create Date: 2023-03-14 16:13:23.809226

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '4ee0e23d96da'
down_revision = '2381a77e8487'
branch_labels = None
depends_on = None


def upgrade() -> None:
    for name in (
        "test_anom_mean",
        "test_vorticity",
        "test_double_diff",
        "test_dot_product",
        "test_map_overlap_sample",
    ):
        op.execute(
            f"""
            update test_run 
            set name = '{name}[uncompressible]',
            path = 'benchmarks/test_array.py'
            where name == '{name}';
            """
        )
    op.execute(
        """
        delete from test_run
        where path = 'benchmarks/test_spill.py'
        and name in (
            'test_dot_product_spill[compressible]',
            'test_spilling[compressible-keep]',
            'test_spilling[compressible-release]'
        )
        """
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###