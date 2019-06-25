# -*- coding: utf-8 -*-
import os
import shutil

import git
from jinja2 import Environment, FileSystemLoader
from virtualenv import create_environment

from pyscaffold import current_path
from pyscaffold.exc import ProjectDirAlreadyExist

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


def scaffold(name='unknown', description='none', git=False, venv=False):
    project_root_dir = os.path.join(os.getcwd(), '{}'.format(name))
    try:
        if os.path.exists(project_root_dir):
            raise ProjectDirAlreadyExist('project directory already exist: {}'.format(project_root_dir))
        create_project_dir(project_root_dir, name, description)
        if git:
            git_init(project_root_dir)
        if venv:
            create_virtualenv(project_root_dir)
        return project_root_dir
    except Exception as e:
        if isinstance(e, ProjectDirAlreadyExist):
            pass
        else:
            if os.path.exists(project_root_dir):
                shutil.rmtree(project_root_dir)
        raise
