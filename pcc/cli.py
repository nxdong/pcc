"""Console script for pcc."""
from email.policy import default
import sys
import click
import os

DEFAUTL_JOBS_COUNT = max(1, os.cpu_count()-2)


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@click.command()
@click.argument('code_path', type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True, resolve_path=True, allow_dash=False))
@click.option('-j', '--jobs', type=int, default=DEFAUTL_JOBS_COUNT, show_default=True, help="Greet the world.")
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def main(code_path, jobs):
    """Cyclomatic Complexity Caculator"""
    click.echo("code_path:")
    click.echo(click.format_filename(code_path))

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
