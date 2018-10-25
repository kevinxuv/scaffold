# -*- coding: utf-8 -*-
import os

import click
from jinja2 import Environment, FileSystemLoader

current_path = os.path.dirname(os.path.realpath(__file__))

def create_project_dir(name, description):
    project_root_dir = './{}'.format(name)
    project_package_dir = project_root_dir + '/{}'.format(name)
    os.makedirs(project_package_dir)
    env = Environment(loader=FileSystemLoader(current_path + '/templates'))
    with open(project_package_dir + '/__init__.py', 'wb') as fh:
        fh.write(env.get_template('__init__.py.jinja').render())
    with open(project_root_dir + '/README.md', 'wb') as fh:
        fh.write(env.get_template('README.md.jinja').render(project=name, description=description))
    open(project_root_dir + '/requirements.txt', 'w+')
    return project_root_dir


@click.command()
def run():
    name = click.prompt('give your project a name', default='unknown', type=str)
    description = click.prompt('write a description of your project', default='none', type=str)
    create_project_dir(name, description)
    click.echo('finish scaffold project {}'.format(name))


if __name__ == '__main__':
    run()
