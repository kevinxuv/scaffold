from setuptools import setup, find_packages


setup(
    name='scaffold',
    version='0.1.0',
    url='https://github.com/kevinxuv/scaffold',
    description='scaffold python project',
    author='kevin.xu.v',
    license='BSD',
    packages=find_packages(exclude=('tests', 'tests.*')),
    package_data={'scaffold': ['templates/*']},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['scaf = scaffold.cli:run']
    },
    classifiers=[
        'Framework :: scaffold',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7'
    ],
    install_requires=[
        'click==7.0',
        'jinja2==2.11.3',
        'gitpython==3.1.2',
        'virtualenv==20.0.20',
        'flask==1.0.2'
    ],
)
