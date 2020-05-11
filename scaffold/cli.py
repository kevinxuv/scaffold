# -*- coding: utf-8 -*-
import logging

import click

from scaffold.core import scaffold


logger = logging.getLogger(__name__)


@click.command()
def run():
    name = click.prompt(
        '-> give your project a name', default='unknown', type=str)
    description = click.prompt(
        '-> write a description for your project', default='none', type=str)
    git = click.prompt('-> init git or not?', default=False, type=bool)
    # venv = click.prompt('-> create virtualenv or not?', default=False, type=bool)
    click.echo(click.style('Start to scaffold project...', fg='blue', bold=True))
    try:
        project_root_dir = scaffold(name=name, description=description, git=git)
        click.echo(
            click.style(
                f'Finish scaffolding project {name} at {project_root_dir}',
                fg='blue',
                bold=True
            )
        )
    except Exception as e:
        logger.exception(e)
        click.echo(
            click.style(
                f'[ERROR] failed to scaffold project: {e}',
                fg='red',
                bold=True
            )
        )


if __name__ == '__main__':
    run()
