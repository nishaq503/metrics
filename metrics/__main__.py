import polars

from metrics.utils import constants

sub_dirs = ["fashion-mnist", "euclidean"]
report_dir = constants.DATA_ROOT.joinpath(*sub_dirs)
tree_path = report_dir.joinpath("tree.arrow")
leaves_path = report_dir.joinpath("leaves.arrow")
distances_path = report_dir.joinpath("query-distances-batch-1-1.npy")

df = polars.scan_ipc(tree_path)
