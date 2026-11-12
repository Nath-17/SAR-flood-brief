import importlib
from importlib.metadata import version

import pytest

import floodbrief

SUBPACKAGES = ["data", "models"]


def test_version():
    assert isinstance(floodbrief.__version__, str)
    assert floodbrief.__version__
    assert floodbrief.__version__ == version("floodbrief")


@pytest.mark.parametrize("name", SUBPACKAGES)
def test_subpackage_imports(name):
    module = importlib.import_module(f"floodbrief.{name}")
    assert module.__name__ == f"floodbrief.{name}"
