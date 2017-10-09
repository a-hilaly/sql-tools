from setuptools import setup, find_packages, Command

class run_tests(Command):
    """Runs all "PYTHON" tests under $/tests folder
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
        from mysql_utils.tests.run_tests import run_all_tests
        run_all_tests()
"""
class configure(Command):

    #Runs all "PYTHON" tests under the

    # distutils complains if this is not here.
    description = "run all tests"
    user_options = [('host', None, 'Set localhost'),
                    ('user', None, 'Set user name'),
                    ('password', None, 'Set password'),
                    ('port', None, 'Set Port')]

    def __init__(self, *args):
        self.args = args[0]  # so we can pass it to other classes
        Command.__init__(self, *args)

    def initialize_options(self):  # distutils wants this
        self.host = None
        self.user = None
        self.password = None
        self.port = None

    def finalize_options(self):    # this too
        pass

    def run(self):
        print(self.host, self.user, self.password, self.port)
"""

setup(
    name='mysql-utils',
    version='0.4.0',
    description='Mysql utilities',
    author='M.A-Hilaly',
    author_email='hilalyamine@gmail.com',
    cmdclass={'test' : run_tests},
    packages=find_packages(exclude=('tests', 'docs'))
)
