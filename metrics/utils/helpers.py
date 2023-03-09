import pathlib
import typing


def get_sub_dirs(path: pathlib.Path) -> typing.Generator[pathlib.Path, None, None]:
    yield from filter(lambda p: p.is_dir(), path.iterdir())


def get_sub_paths(path: pathlib.Path) -> typing.Generator[pathlib.Path, None, None]:
    yield from filter(lambda p: not p.is_dir(), path.iterdir())
