"""Select cells without physical parameters from Network Live db."""

import os
from collections import namedtuple

import cx_Oracle
from dotenv import load_dotenv

load_dotenv('.env')

gsm_select = """
    SELECT
        operator,
        bscname,
        sitename,
        cell
    FROM
        gsmcells2
    WHERE
        azimut is null
"""

wcdma_select = """
    SELECT
        operator,
        rncname,
        sitename,
        utrancell
    FROM
        wcdmacells2
    WHERE
        azimut is null
"""

lte_select = """
    SELECT
        subnetwork,
        sitename,
        eutrancell
    FROM
        ltecells2
    WHERE
        azimut is null
"""

nr_select = """
    SELECT
        subnetwork,
        sitename,
        cellname
    FROM
        nrcells
    WHERE
        azimut is null
"""


def execute_sql_command(sql_command, row_factory):
    """
    Execute SQL command and fetch rows with given row_factory.

    Args:
        sql_command: string
        row_factory: object with needed stucture

    Returns:
        object according to row_factory
    """
    atoll_dsn = cx_Oracle.makedsn(
        os.getenv('ATOLL_HOST'),
        os.getenv('ATOLL_PORT'),
        service_name=os.getenv('SERVICE_NAME'),
    )
    with cx_Oracle.connect(
        user=os.getenv('ATOLL_LOGIN'),
        password=os.getenv('ATOLL_PASSWORD'),
        dsn=atoll_dsn,
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(sql_command)
        cursor.rowfactory = row_factory
        return cursor.fetchall()


def parse_columns(sql_select):
    """
    Parse selecting columns from sql_select command.

    Args:
        sql_select: string

    Returns:
        list with columns
    """
    sql_command_without_spaces = sql_select.replace(' ', '')
    sql_command_without_commas = sql_command_without_spaces.replace(',', '')
    sql_command_list = sql_command_without_commas.split('\n')
    return sql_command_list[
        sql_command_list.index('SELECT') + 1:sql_command_list.index('FROM')
    ]


def select_cells():
    """
    Select cells from Network Live db without physical params.

    Returns:
        dict
    """
    sql_data = {
        'gsm': [gsm_select, namedtuple('GsmCells', parse_columns(gsm_select))],
        'wcdma': [wcdma_select, namedtuple('WcdmaCells', parse_columns(wcdma_select))],
        'lte': [lte_select, namedtuple('LteCells', parse_columns(lte_select))],
        'nr': [nr_select, namedtuple('NrCells', parse_columns(nr_select))],
    }

    selected_data = {}

    for tech, sql_params in sql_data.items():
        sql_select, row_factory = sql_params
        selected_data[tech] = execute_sql_command(sql_select, row_factory)

    return selected_data
