"""Get cells configured in the network, but missing in atoll and send report."""

from network_vs_atoll.excel import fill_excel
from network_vs_atoll.report import make_report
from network_vs_atoll.select_data import select_cells
from network_vs_atoll.send_mail import send_email


def main():
    """Get cells configured in the network, but missing in atoll and send report."""
    report_path = 'reports/network-vs-atoll.xlsx'
    selected_data = select_cells()
    report_message = make_report(selected_data)
    fill_excel(selected_data, report_path)

    to_addr = 'ramil.albakov@kcell.kz'
    send_email(
        to_addr,
        'Network vs Atoll',
        report_message,
        report_path,
    )
