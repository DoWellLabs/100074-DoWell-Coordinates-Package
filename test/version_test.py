
# import pytest   # type
from utils.version import __version__


def test_version() -> None:
    """
    Unit Test for version file
    """
    assert __version__ == '0.1.0', 'version should be 0.1.0'
