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
        from sql_tools.tests.run_tests import run_all_tests
        run_all_tests()


setup(
    name='sql_tools',
    version='0.4.0',
    description='Mysql utilities',
    author='M.A-Hilaly',
    author_email='hilalyamine@gmail.com',
    cmdclass={'test' : run_tests},
    packages=find_packages(),
    package_data={'sql_tools': ['config/mysql_conf.ini']},
    include_package_data=True,
    zip_safe=False,
)
