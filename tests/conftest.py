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
            LteCells('subnet1', 'lsite1', 'L2100cell'),
            LteCells('subnet2', 'ERBS_555', 'L1800'),
            LteCells('subnet3', 'ERBS_777', 'cell3'),
        ],
    }
