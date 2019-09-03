#!/usr/bin/env python


def convert_as_table_format(column_names, contents, line_separator='\n', separator='|'):
    table_header = convert_as_row_format(column_names)
    divider_tail = ' ------ {0}'.format(separator) * len(column_names)
    divider = '{0}{1}'.format(separator, divider_tail)
    rows = [convert_as_row_format(row_items, separator) for row_items in contents]
    return line_separator.join([table_header, divider, *rows])


def convert_as_row_format(items, separator='|'):
    escaped_separator = '\{0}'.format(separator)
    margin_separator = ' {0} '.format(separator)
    body = margin_separator.join(str(item).replace(separator, escaped_separator) for item in items)
    res = "{0} {1} {2}".format(separator, body, separator)
    return res
