"""Filter selected data."""


def filter_lte(lte_cells):
    """
    Filter lte_cells from Beeline cells on Ericsson equipment.

    Args:
        lte_cells: list

    Returns:
        list
    """
    return list(filter(
        lambda cell: not (cell.sitename.startswith('ERBS_') and cell.eutrancell.startswith('L')),
        lte_cells,
    ))
