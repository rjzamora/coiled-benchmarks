
LOCAL_SF1_PATH = "/raid/dask-space/rzamora/tpch-data/tables_scale_1/"
LOCAL_SF10_PATH = "/raid/dask-space/rzamora/tpch-data/tables_scale_10/"
LOCAL_SF100_PATH = "/raid/dask-space/rzamora/tpch-data/tables_scale_100/"


def get_dataset_path(local, scale):
    remote_paths = {
        1: "s3://coiled-runtime-ci/tpc-h/snappy/scale-1/",
        10: "s3://coiled-runtime-ci/tpc-h/snappy/scale-10/",
        100: "s3://coiled-runtime-ci/tpc-h/snappy/scale-100/",
        1000: "s3://coiled-runtime-ci/tpc-h/snappy/scale-1000/",
        10000: "s3://coiled-runtime-ci/tpc-h/snappy/scale-10000/",
    }
    local_paths = {
        #1: "./tpch-data/scale-1/",
        1: LOCAL_SF1_PATH,
        #10: "./tpch-data/scale-10/",
        10: LOCAL_SF10_PATH,
        #100: "./tpch-data/scale-100/",
        100: LOCAL_SF100_PATH,
    }

    if local:
        return local_paths[scale]
    else:
        return remote_paths[scale]
