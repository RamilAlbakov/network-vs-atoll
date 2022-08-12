"""Test functions from report module."""

from network_vs_atoll.report import make_report


def test_make_report():
    """Test make_report function."""
    selected_data = {
        'gsm': [('bsc1', 'site1', 'cell1'), ('bsc1', 'site2', 'cell2')],
        'lte': [('site1', 'cell1'), ('site2', 'cell2'), ('site3', 'cell3')],
    }

    message = make_report(selected_data)
    cells_info = message.split('\n')[1:-1]
    expected = ['gsm: 2', 'lte: 3']

    assert cells_info == expected
