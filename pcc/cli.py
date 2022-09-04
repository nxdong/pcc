"""Console script for pcc."""
from locale import currency
from pydoc import cli
import sys
from time import time
import typing
import click
import os
import requests
from rich.console import Console
from rich.table import Table
from rich import box
import pcc
from pcc.config import PCC_LIB_PATH
from pcc.config import PCC_LIB_NAME
from pcc.config import PCC_DEFAULT_LIB_URL
from pcc.config import DEFAUTL_JOBS_COUNT
from pcc.config import DEFAUTL_RESULT_COUNT
from pcc.config import FILE_EXT_MAP
from .utils import travel_dir_and_filter
import concurrent.futures
import time


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 0.0.1')
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


def echo_result(results: typing.Mapping[str, typing.List], limits_count: int = DEFAUTL_RESULT_COUNT, sort_by_cc: bool = True):
    # merge file result
    total_list = []
    for _file, v in results.items():
        total_list += v
    # sort
    if sort_by_cc:
        total_list = sorted(
            total_list, key=lambda x: x.complexity(), reverse=True)
        if limits_count > 0:
            total_list = total_list[0:limits_count]
        print_retsult_table(total_list)
    else:
        if limits_count > 0:
            total_list = total_list[0:limits_count]
        print_retsult_table(total_list)


def process_file(code_path: str):
    ret = pcc.calc_code_complexity_from_file(code_path)
    return {code_path: ret}


def run_in_threadpool(file_lists: typing.List[str], jobs: int):
    ret = {}
    with concurrent.futures.ProcessPoolExecutor(max_workers=jobs) as executor:
        results = executor.map(process_file, file_lists)
        for result in results:
            ret.update(result)
    return ret


@click.command()
@click.argument('code_path', type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True, resolve_path=True, allow_dash=False))
@click.option('-j', '--jobs', type=int, default=DEFAUTL_JOBS_COUNT, show_default=True, help="Parallel jobs count")
@click.option('-c', '--count', type=int, default=DEFAUTL_RESULT_COUNT, show_default=True, help="Output item count")
@click.option('-s', '--sort', type=bool, default=True, show_default=True, help="sort by Complexity")
@click.option('-e', '--exclude_path', envvar="PCC_EXCLUDE_PATH", type=click.Path(file_okay=False, dir_okay=True, readable=True, resolve_path=True, allow_dash=False), multiple=True, help="exclude path")
@click.option('--lib_path', envvar="PCC_LIB_PATH", type=click.Path(file_okay=False, dir_okay=True, readable=True, resolve_path=True, allow_dash=False), default=PCC_LIB_PATH, show_default=True, help="tree-sitter library path")
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def main(code_path, jobs, count, sort, exclude_path, lib_path):
    """Cyclomatic Complexity Caculator"""
    check_or_download(lib_path)
    if os.path.isdir(code_path):
        t1 = time.time()
        code_paths = travel_dir_and_filter(
            code_path, exclude_path, FILE_EXT_MAP)
        ret = run_in_threadpool(code_paths, jobs)
        echo_result(ret, limits_count=count, sort_by_cc=sort)
        t2 = time.time()
        click.secho("Procee [{}] files use Time: {} s".format(
            len(code_paths), t2-t1))
    else:
        ret = pcc.calc_code_complexity_from_file(code_path)
        ret = {code_path: ret}
        echo_result(ret, limits_count=count, sort_by_cc=sort)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
