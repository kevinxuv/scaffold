# -*- coding: utf-8 -*-

import click

from scaffold.core import scaffold


@click.command()
def run():
    name = click.prompt(
        'give your project a name', default='unknown', type=str)
    description = click.prompt(
        'write a description of your project', default='none', type=str)
    git = click.prompt('init git or not?', default=False, type=bool)
    venv = click.prompt('create virtualenv or not?', default=False, type=bool)
    try:
        project_root_dir = scaffold(
            name=name, description=description, git=git, venv=venv)
        click.echo(
            click.style(
                'Finish scaffolding project {} at {}'.format(name, project_root_dir),
                fg='blue',
                bold=True
            )
        )
    except Exception as e:
        click.echo(
            click.style(
                '[ERROR] failed to scaffold project: {}'.format(str(e)),
                bg='red',
                bold=True
            )
        )


if __name__ == '__main__':
    run()
