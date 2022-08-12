"""Prepare report with statistics which will be used as email message."""


def make_report(selected_data):
    """
    Make a report message about selected cells missing in atoll by technology.

    Args:
        selected_data: dict with namedtuple for each technology

    Returns:
        string
    """
    all_cells_count = {tech: len(cells) for tech, cells in selected_data.items()}
    message = 'Below the number of cells configured on the network, but absent in atoll:'

    for tech, cells_count in all_cells_count.items():
        message = '{message}\n{tech}: {cells_count}'.format(
            message=message,
            tech=tech,
            cells_count=cells_count,
        )
    return '{message}\nFull list of the cells is in the attachment'.format(
        message=message,
    )
