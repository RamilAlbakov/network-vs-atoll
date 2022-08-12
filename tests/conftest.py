"""Custom fixtures for tests."""

import pytest

from collections import namedtuple


@pytest.fixture()
def selected_data():
    """
    Prepare data which will be selected from db.

    Returns:
        dict
    """

    GsmCells = namedtuple('GsmCells', ['operator', 'bscname', 'sitename', 'cell'])
    LteCells = namedtuple('LteCells', ['subnetwork', 'sitename', 'eutrancell'])

    return {
        'gsm': [
            GsmCells('kcell', 'bsc1', 'site1', 'cell1'),
            GsmCells('bee', 'bsc2', 'site2', 'cell2'),
        ],
        'lte': [
            LteCells('subnet1', 'lsite1', 'lcell1'),
            LteCells('subnet2', 'lsite2', 'lcell2'),
            LteCells('subnet3', 'lsite3', 'lcell3'),
        ],
    }
