# -*- coding: utf-8 -*-

import click

from pyscaf.core import scaf


@click.command()
def run():
    name = click.prompt(
        'give your project a name', default='unknown', type=str)
    description = click.prompt(
        'write a description of your project', default='none', type=str)
    git = click.prompt('init git or not?', default=False, type=bool)
    venv = click.prompt('create virtualenv or not?', default=False, type=bool)
    try:
        scaf(name=name, description=description, git=git, venv=venv)
        click.echo(
            click.style(
                'Finish scaffolding project {}...'.format(name),
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
