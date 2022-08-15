"""Check the cells configured in the network, but missing in atoll and send report."""

from dotenv import load_dotenv
from network_vs_atoll.main import main

load_dotenv('.env')


def main_script():
    """Check the cells configured in the network, but missing in atoll and send report."""
    main()
