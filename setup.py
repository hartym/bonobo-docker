# This file is autogenerated by medikit code generator.
# All changes will be overwritten.

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Py3 compatibility hacks, borrowed from IPython.
try:
    execfile
except NameError:

    def execfile(fname, globs, locs=None):
        locs = locs or globs
        exec(compile(open(fname).read(), fname, "exec"), globs, locs)


# Get the long description from the README file
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

# Get the classifiers from the classifiers file
tolines = lambda c: list(filter(None, map(lambda s: s.strip(), c.split('\n'))))
try:
    with open(path.join(here, 'classifiers.txt'), encoding='utf-8') as f:
        classifiers = tolines(f.read())
except:
    classifiers = []

version_ns = {}
try:
    execfile(path.join(here, 'bonobo_docker/_version.py'), version_ns)
except EnvironmentError:
    version = 'dev'
else:
    version = version_ns.get('__version__', 'dev')

setup(
    author='Romain Dorgueil',
    author_email='romain@dorgueil.net',
    description='Docker extension for Bonobo',
    license='Apache License, Version 2.0',
    name='bonobo_docker',
    version=version,
    long_description=long_description,
    classifiers=classifiers,
    packages=find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data=True,
    install_requires=['bonobo (~= 0.6.0a2)', 'docker (~= 2.7)', 'requests (~= 2.16, < 3.0)'],
    extras_require={
        'dev': [
            'bonobo (~= 0.6.0a2)', 'coverage (>= 4.4, < 5.0)', 'pytest (>= 3.1, < 4.0)', 'pytest-cov (>= 2.5, < 3.0)',
            'sphinx (>= 1.6, < 2.0)', 'yapf'
        ]
    },
    entry_points={'bonobo.commands': ['runc = bonobo_docker.commands.runc:register']},
    url='https://www.bonobo-project.org/with/docker',
    download_url='https://github.com/python-bonobo/bonobo-docker/tarball/{version}'.format(version=version),
)
