"""Dump report into fixed format worksheets of a workbook from Redmond near Seattle, WA, USA."""
# import json
# import pathlib
# import sys
# from datetime import date
# from time import time
from typing import no_type_check

import pandas as pd  # type: ignore
import xlsxwriter  # type: ignore

COL_SEP = ';'
ENCODING = 'utf-8'
ROW_INDEX_HEADERS = 0
ROW_INDEX_CONTENT_START = 1


@no_type_check
def dump_row(sheet, row, entries=None):
    """Dump data into indicated row."""
    for col, entry in enumerate([] if entries is None else entries, start=0):
        sheet.write(row, col, entry)


@no_type_check
def add_sheet(workbook, name, headers):
    """Add a sheet, fill in headers, and return the handle."""
    sheet = workbook.add_worksheet(name)
    dump_row(sheet, row=ROW_INDEX_HEADERS, entries=headers)
    return sheet


def fill_sheet(sheet, matrix):
    """Dump data into the content area of the sheet#s table."""
    if not matrix:
        return

    for row, entries in enumerate(matrix, start=ROW_INDEX_CONTENT_START):
        dump_row(sheet, row, entries=entries)


@no_type_check
def update_totals_table(total_worksheet, folder_count, files_count, aspect_counts):
    """Update the worksheet total with a table containing the key-value pairs per file type and folder."""
    dump_row(total_worksheet, ROW_INDEX_HEADERS, ['key', 'value'])
    key_col_index = 0
    value_col_index = 1

    row = ROW_INDEX_CONTENT_START
    total_worksheet.write(row, key_col_index, 'folder')
    total_worksheet.write(row, value_col_index, folder_count)

    row += 1
    total_worksheet.write(row, key_col_index, 'file')
    total_worksheet.write(row, value_col_index, files_count)

    row += 1
    for kv_row, (key, value) in enumerate(aspect_counts.items(), start=row):
        total_worksheet.write(kv_row, key_col_index, f'file.{key}')
        total_worksheet.write(kv_row, value_col_index, aspect_counts.get(value, 0))


@no_type_check
def create_book(path):
    """Create a workbook at path and return the handle."""
    return xlsxwriter.Workbook(path)


@no_type_check
def add_sheets(book, facets):
    """Add sheets for the facets and return a dict of sheet handles with the facets and a special total key."""
    return {
        **{facet: add_sheet(book, facet) for facet in facets},
        'total': book.add_worksheet('total'),
    }


@no_type_check
def close_book(handle):
    """Attempt to close the book per handle and assume any exception is due to file locking."""
    try:
        handle.close()
    except Exception:  # pylint: disable=broad-except
        print(
            'The spreadsheet file is locked - possibly in use by another application.'
            ' Please close the other app and execute again.'
        )
        return 1


@no_type_check
def derive_csv(counter, path, out_folder):
    """Derive a single CSV file for counter from workbook at path writing to out folder and per convention."""
    table = pd.read_excel(path, counter)
    table.to_csv(out_folder / f'{counter}.csv', COL_SEP)


@no_type_check
def derive_csvs(counters, path, out_folder):
    """Somehow clumsy derivation of CSV files from counters and main workbook at path."""
    for counter in counters:
        if counter not in ('folder', 'other') and counters[counter]:
            derive_csv(counter, path, out_folder)
