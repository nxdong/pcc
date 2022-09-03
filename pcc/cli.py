"""Console script for pcc."""
import sys
import typing
import click
import os
import pcc
from pcc.config import PCC_LIB_PATH
from pcc.config import PCC_LIB_NAME
from .config import PCC_DEFAULT_LIB_URL
import requests
from rich.console import Console
from rich.table import Table
from rich import box

DEFAUTL_JOBS_COUNT = max(1, os.cpu_count()-2)


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


def download_library(target_file_path):
    data = requests.get(PCC_DEFAULT_LIB_URL)
    with open(target_file_path, 'wb') as f:
        f.write(data.content)


def check_or_download(lib_path: str):
    library_path = os.path.join(lib_path, PCC_LIB_NAME)

    if os.path.exists(lib_path):
        if not os.path.exists(library_path):
            if click.confirm('Do you want to dowload one from [{}] ?'.format(library_path)):
                download_library(library_path)
                click.secho('Download [{}] success!'.format(
                    lib_path), fg='green')
            else:
                exit(-1)
    else:
        if click.confirm('Do you want to creat [{}] ?'.format(lib_path)):
            os.makedirs(lib_path)
            click.secho('Create Dir [{}] success!'.format(
                lib_path), fg='green')
            if click.confirm('Do you want to dowload one from [{}] ?'.format(library_path)):
                download_library(library_path)
                click.secho('Download [{}] success!'.format(
                    lib_path), fg='green')
        else:
            exit(-1)

    # check library success
    PCC_LIB_PATH = lib_path


def print_retsult_table(total_list: typing.List):
    table = Table(title="Code Cyclomatic Complexity Caculator",
                  box=box.MARKDOWN)

    table.add_column("Complexity", justify="right",
                     style="cyan", no_wrap=True)
    table.add_column("Function", justify="left", style="magenta")
    table.add_column("File", justify="right", style="green")

    for item in total_list:
        func = item.name.split(":")[0]
        table.add_row(str(item.complexity()), func,
                      item.filename + ':'+str(item.lineno))
    console = Console()
    console.print(table)


def echo_result(results: typing.Mapping[str, typing.List], limits: int = 10, sort_by_cc: bool = True):
    if sort_by_cc:
        total_list = []
        for file, v in results.items():
            total_list += v
        total_list = sorted(
            total_list, key=lambda x: x.complexity(), reverse=True)
        if limits > 0:
            total_list = total_list[0:limits]
        print_retsult_table(total_list)
    else:
        pass


@click.command()
@click.argument('code_path', type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True, resolve_path=True, allow_dash=False))
@click.option('-j', '--jobs', type=int, default=DEFAUTL_JOBS_COUNT, show_default=True, help="Greet the world.")
@click.option('--lib_path', envvar="PCC_LIB_PATH", type=click.Path(file_okay=False, dir_okay=True, readable=True, resolve_path=True, allow_dash=False), default=PCC_LIB_PATH, show_default=True, help="tree-sitter library path")
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def main(code_path, jobs, lib_path):
    """Cyclomatic Complexity Caculator"""
    # click.echo("code_path:")
    # click.echo(click.format_filename(code_path))
    # print("code path:", code_path)
    # print("code path type:", type(code_path))
    # print("lib path:", lib_path)
    # check if library
    check_or_download(lib_path)

    if os.path.isdir(code_path):
        pass
    else:
        ret = pcc.calc_code_complexity_from_file(code_path)
        for i in range(len(ret)):
            ret[i].filename = code_path
        ret = {code_path: ret}
        echo_result(ret)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
