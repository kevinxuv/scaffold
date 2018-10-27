# -*- coding: utf-8 -*-
import click

from pyscaf.core import create_project_dir

@click.command()
def run():
    name = click.prompt('give your project a name', default='unknown', type=str)
    description = click.prompt('write a description of your project', default='none', type=str)
    try:
        create_project_dir(name, description)
        click.echo(
            click.style(
                'success to scaffold project {}'.format(name), 
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
        click.Abort()


if __name__ == '__main__':
    run()
