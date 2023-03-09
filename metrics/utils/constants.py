import pathlib

PKG_ROOT = pathlib.Path(__file__).parents[2].resolve()
DATA_ROOT = PKG_ROOT.joinpath("data").resolve()

FIGURES_ROOT = PKG_ROOT.joinpath("figures")
FIGURES_ROOT.mkdir(exist_ok=True)
