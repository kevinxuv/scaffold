# -*- coding: utf-8 -*-
import os
import shutil

import click

from pyscaf.core import create_project_dir, git_init, create_virtualenv
from pyscaf.exc import ProjectDirAlreadyExist


@click.command()
def run():
    name = click.prompt(
        'give your project a name', default='unknown', type=str)
    description = click.prompt(
        'write a description of your project', default='none', type=str)
    git = click.prompt('init git or not?', default=False, type=bool)
    venv = click.prompt('create virtualenv or not?', default=False, type=bool)

    project_root_dir = os.path.join(os.getcwd(), '{}'.format(name))
    try:
        if os.path.exists(project_root_dir):
            raise ProjectDirAlreadyExist('project folder already exist')
        create_project_dir(project_root_dir, name, description)
        if git:
            git_init(project_root_dir)
        if venv:
            venv_path = create_virtualenv(project_root_dir)
            click.echo(
                click.style(
                    'success to create project virtualenv path: ' + venv_path,
                    fg='blue'
                )
            )

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
        if isinstance(e, ProjectDirAlreadyExist):
            return
        if os.path.exists(project_root_dir):
            shutil.rmtree(project_root_dir)


if __name__ == '__main__':
    run()
