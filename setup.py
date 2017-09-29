from setuptools import setup, find_packages, Command

class run_tests(Command):
    pass

setup(
    name='mysql-glob',
    version='0.0.1',
    description='null',
    author='null',
    author_email='0@None.null',
    packages=find_packages(exclude=('tests', 'docs'))
)
