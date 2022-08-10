"""Test functions from select_data module."""

from network_vs_atoll.select_data import parse_columns


def test_parse_columns():
    """Test parse_columns function."""
    select_command = """
        SELECT
            col1,
            col2,
            col3
        FROM
            table
    """
    assert parse_columns(select_command) == ['col1', 'col2', 'col3']
