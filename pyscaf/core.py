# -*- coding: utf-8 -*-
import os

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
