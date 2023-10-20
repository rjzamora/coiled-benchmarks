from . import test_dask  # noqa: F401

try:
    from . import test_duckdb, test_polars, test_pyspark  # noqa: F401
except ImportError:
    pass
