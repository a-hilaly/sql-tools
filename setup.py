from setuptools import setup, find_packages, Command

class run_tests(Command):
    """Runs all "PYTHON" tests under the greww/folder
    """

    description = "run all tests"
    user_options = []  # distutils complains if this is not here.

    def __init__(self, *args):
        self.args = args[0]  # so we can pass it to other classes
        Command.__init__(self, *args)

    def initialize_options(self):  # distutils wants this
        pass

    def finalize_options(self):    # this too
        pass

    def run(self):
        from mysql_glob.tests.run_tests import run_all_tests
        run_all_tests()

setup(
    name='mysql-glob',
    version='0.0.1',
    description='null',
    author='null',
    author_email='0@None.null',
    cmdclass={'test' : run_tests},
    packages=find_packages(exclude=('tests', 'docs'))
)
