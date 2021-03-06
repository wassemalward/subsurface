import pytest
import pandas as pd
from subsurface.io import faults
from subsurface.fault import FaultSticks


@pytest.fixture(scope="module")
def get_faultsticks() -> pd.DataFrame:
    fp = "./data/faultsticks"
    faultsticks = faults.read_faultsticks_charisma(fp)
    return faultsticks


def test_faultsticks_npoints(get_faultsticks):
    assert len(get_faultsticks) == 12


def test_faultsticks_nsticks(get_faultsticks):
    assert len(get_faultsticks["stick id"].unique()) == 4


def test_FaultSticks(get_faultsticks):
    """Test instantiation of FaultSticks class."""
    fault = FaultSticks(get_faultsticks)