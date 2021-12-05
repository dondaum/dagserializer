import argparse
import sys

from rich import print

from dagserializer import flags

DESC = """
This library contains a dbt supporting package for the EDW-Flow
automation tool. It offers some convience functionality that
helps to speed up EDW-Flow development.
"""

LOGO = r"""
     _                           _       _ _              
    | |                         (_)     | (_)             
  __| | __ _  __ _ ___  ___ _ __ _  __ _| |_ _______ _ __ 
 / _` |/ _` |/ _` / __|/ _ \ '__| |/ _` | | |_  / _ \ '__|
| (_| | (_| | (_| \__ \  __/ |  | | (_| | | |/ /  __/ |   
 \__,_|\__,_|\__, |___/\___|_|  |_|\__,_|_|_/___\___|_|   
              __/ |                                       
             |___/ 
"""


def dummy():
    return ""


def _build_base_subparser() -> argparse.ArgumentParser:
    """
    Function that creates the base suparser
    """
    base_subparser = argparse.ArgumentParser(add_help=False)

    base_subparser.add_argument(
        "-t",
        "--db_name",
        type=str,
        help=("Name of the target Snowflake clone database "),
        required=False,
    )

    base_subparser.add_argument(
        "-l",
        "--logging_level",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"],
        default="WARNING",
        type=str,
        help=(
            "Required logging level for dbtspeed:"
            "CRITICAL, ERROR, WARNING, INFO, DEBUG"
        ),
        required=False,
    )

    base_subparser.add_argument(
        "--threads",
        type=int,
        required=False,
        help="""
        Specify number of threads Overrides settings in profiles.yml.
        """,
    )

    base_subparser.add_argument(
        "--table_result",
        action="store_true",
        help="""
        Show a table with the query result
        """,
    )
    return base_subparser


def _build_clone_subparser(
    subparsers, base_subparser
) -> argparse.ArgumentParser:
    """
    Function that creates the clone subparser
    """
    clone_sub = subparsers.add_parser(
        "clone",
        parents=[base_subparser],
        help="""
        Expect that a dev database existing with an naming
        logic that can be used to use the Snowflake cone
        feature to clone only database tables from a source
        database to a dev target database
        """,
    )
    clone_sub.set_defaults(
        callable=dummy,
        which="clone",
    )
    return clone_sub


def cmdline_args(args) -> argparse.Namespace:
    """
    Function that generates the main Argument Parser
    and subparsers
    """
    p = argparse.ArgumentParser(
        prog="dbtspeed", add_help=True, description=DESC
    )

    subparsers = p.add_subparsers(help="Available subparsers")

    base_subparser = _build_base_subparser()

    _build_clone_subparser(subparsers, base_subparser)
    return p.parse_args(args)


def load_cli() -> None:
    """
    Function that loads the cli. Is the main
    entrypoint for the cli
    """
    print(LOGO)
    parsed = cmdline_args(sys.argv[1:])
    run(parsed)


def run(parsed=None) -> None:
    """
    Generic run method that needs to be changed
    for specific use cases. It expects that all
    class tasks must have a run method.
    """
    flags.set_from_args(parsed)
    if "callable" in dir(parsed):
        method_name = parsed.callable
        print(method_name)
        return method_name()

    if "cls" in dir(parsed):
        klass_name = parsed.cls
        results = klass_name(**vars(parsed)).run()
        return results


if __name__ == "__main__":
    load_cli()
