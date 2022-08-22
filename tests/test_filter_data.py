"""Test functions from filter_data module."""

from network_vs_atoll.filter_data import filter_lte


def test_filter_lte(selected_data):
    filtered_cells = filter_lte(selected_data['lte'])

    assert len(filtered_cells) == 2
    assert filtered_cells[0].eutrancell == 'L2100cell'
    assert filtered_cells[1].sitename == 'ERBS_777'