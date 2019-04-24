from setuptools import setup, find_packages


setup(
    name='pyscaf',
    version='0.1.0',
    url='https://github.com/kevinxuv/pyscaf',
    description='scaffold python project',
    author='kevin.xu.v',
    license='BSD',
    packages=find_packages(exclude=('tests', 'tests.*')),
    package_data={'pyscaf':['templates/*']},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['scaf = pyscaf.cli:run']
    },
    classifiers=[
        'Framework :: scaf',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'click==7.0',
        'jinja2==2.10.1',
        'gitpython==2.1.11',
        'virtualenv==16.0.0',
        'flask==1.0.2'
    ],
)
