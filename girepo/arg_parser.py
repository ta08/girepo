#!/usr/bin/env python

import re
import argparse


def full_name_type(value, pattern=re.compile(r"^(( )*[\w\.\-]+( )*/( )*[\w\.\-]+( )*)$")):
    """
    allow the value contains white-space at around words

    https://regex101.com/r/ks59iR/4

    :param value:
    :param pattern:
    :return:
    """
    if not pattern.match(value):
        raise argparse.ArgumentTypeError("the format of name should be like owner/repo")
    return value.replace(' ', '')


def create_argparser(args, sort_keys):
    parser = argparse.ArgumentParser(
        description="""
        Print Git Repositories information with the markdown format for your documents.
        
        This uses github api without authentication. 
        So you could reach the rate-limitation if you use this 60 requests per hour.
        https://developer.github.com/v3/#rate-limiting
        
        Could you take a cup of coffee \U00002615 until recovering if you exceed. 
        """,
        epilog="God bless you.",
        fromfile_prefix_chars="@"
    )
    parser.add_argument('repo_full_names', type=full_name_type, nargs='+',
                        help='the target repositories written like owner/repository')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--asc', dest="asc_key", choices=sort_keys,
                       help='sort by asc with the field')
    group.add_argument('-d', '--desc', dest="desc_key", choices=sort_keys,
                       help='sort by desc with the field')

    return parser.parse_args(args)
