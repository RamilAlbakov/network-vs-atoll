"""Test functions from report module."""

from network_vs_atoll.report import make_report


def test_make_report(selected_data):
    """Test make_report function."""
    message = make_report(selected_data)
    cells_info = message.split('\n')[1:-1]
    expected = ['gsm: 2', 'lte: 3']

    assert cells_info == expected
