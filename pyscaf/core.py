# -*- coding: utf-8 -*-
import os

import git
from jinja2 import Environment, FileSystemLoader
from virtualenv import create_environment

from pyscaf import current_path

env = Environment(loader=FileSystemLoader(current_path + '/templates'))


def create_project_dir(project_root_dir, name, description):
    project_package_dir = project_root_dir + '/{}'.format(name)
    os.makedirs(project_package_dir)
    with open(project_package_dir + '/__init__.py', 'wb') as fh:
        fh.write(env.get_template('__init__.py.jinja').render())
    with open(project_root_dir + '/README.md', 'wb') as fh:
        fh.write(env.get_template(
            'README.md.jinja').render(project=name, description=description)
        )
    open(project_root_dir + '/requirements.txt', 'w+')


def git_init(project_root_dir):
    git.Repo.init(project_root_dir)
    with open(project_root_dir + '/.gitignore', 'wb') as fh:
        fh.write(env.get_template('gitignore.jinja').render())


def create_virtualenv(project_root_dir):
    venv_path = os.path.join(project_root_dir, '.venv')
    create_environment(venv_path)
    return venv_path
