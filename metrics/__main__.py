import polars

from metrics.utils import constants

sub_dirs = ["fashion-mnist", "euclidean"]
report_dir = constants.DATA_ROOT.joinpath(*sub_dirs)
tree_path = report_dir.joinpath("tree.arrow")
leaves_path = report_dir.joinpath("leaves.arrow")
distances_path = report_dir.joinpath("query-distances-batch-1-1.npy")

# Columns: ['name', 'depth', 'left', 'right', 'cardinality', 'arg_center', 'arg_radius', 'radius', 'lfd', 'polar_distance']
tree_df = polars.scan_ipc(tree_path)

# depths: numpy.ndarray = tree_df.select(polars.col("depth")).collect().to_numpy().squeeze()
# radii: numpy.ndarray = tree_df.select(polars.col("radius")).collect().to_numpy().squeeze()
# polar_distances: numpy.ndarray = tree_df.select(polars.col("polar_distance")).collect().to_numpy().squeeze()
# print(depths.shape, radii.shape, polar_distances.shape)

radii = (
    tree_df.groupby("depth")
    .agg(
        [
            polars.col("radius").quantile(0.25).alias("radius_25"),
            polars.col("radius").quantile(0.50).alias("radius_50"),
            polars.col("radius").quantile(0.75).alias("radius_75"),
            polars.col("polar_distance").quantile(0.25).alias("polar_distance_25"),
            polars.col("polar_distance").quantile(0.50).alias("polar_distance_50"),
            polars.col("polar_distance").quantile(0.75).alias("polar_distance_75"),
        ]
    )
    .sort("depth")
    .collect()
)
print(type(radii))
print(radii.head())
