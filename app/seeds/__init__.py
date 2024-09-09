import click
from flask.cli import with_appcontext


@click.command(name="seeder")
@with_appcontext
def mainSeeder():
    pass
