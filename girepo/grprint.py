#!/usr/bin/env python

import logging
import sys

from girepo.arg_parser import create_argparser
from girepo.formatter import convert_as_table_format
from girepo.extractor import extract, default_mapper
from girepo.fetch import fetch_from
from girepo.sort import sort_by


def retrieve_data_from_github(repo_full_names, mapper):
    contents = []
    for repo_full_name in repo_full_names:
        status_code, json = fetch_from(repo_full_name)
        if status_code is 200:
            content = extract(json, mapper)
            contents.append(content)
        else:
            logging.error(json)
    return contents


def main():
    column_names = list(default_mapper.keys())
    parser = create_argparser(sys.argv[1:], column_names)

    contents = retrieve_data_from_github(parser.repo_full_names, default_mapper)
    contents = sort_by(column_names, contents, parser)

    table_format = convert_as_table_format(column_names, contents, parser.headless)

    print(table_format)


if __name__ == '__main__':
    main()
