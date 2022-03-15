"""Console script for first_project."""
import sys
import click


@click.group(help="My first project CLI Utilities on {}".format(sys.executable))
@click.version_option()
def main():
    pass


@main.command()
@click.option('-n', '--name', help='Your name')
def say_hello(name: str):
    """Say hello with you name."""
    print(f"Hello, {name}")



if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
