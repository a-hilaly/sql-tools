import unittest
import time


"""
         69696969                         69696969
       6969    696969                   696969    6969
     969    69  6969696               6969  6969     696
    969        696969696             696969696969     696
   969        69696969696           6969696969696      696
   696      9696969696969           969696969696       969
    696     696969696969             969696969        969
     696     696  96969      _=_      9696969  69    696
       9696    969696      q(-_-)p      696969    6969
          96969696         '_) (_`         69696969
             96            /__/  \            69
             69          _(<_   / )_          96
            6969        (__\_\_|_/__)        9696
"""


class TestFail(Exception):
    pass


test_modules = ['mysql_utils.tests.test_mysql_types',
                'mysql_utils.tests.test_mysql_queries',
                'mysql_utils.tests.test_mysql_loggings',
                'mysql_utils.tests.test_predef_queries']


Succeeded_Test = "[ OK ] ... {0} succeeded ES:{1} with a total run time of : {2} ms"
Failed_Test = "[WARN] ... {0} failed after runing : {1} ms"


def _test_function(func):
    t1 = time.time()
    try:
        exit_status, t2 = func(), time.time()
        print(Succeeded_Test.format(func.__name__, exit_status, t2 - t1))
        return True
    except:
        t2 = time.time()
        print(Failed_Test.format(func.__name__, t2 - t1))
        return False


def import_module_tests_functions(module):
    mod = __import__(module, globals(), locals(), [''])
    functions = getattr(mod, '__all__')         #XXX: Python need this usless arguments
    return functions                            # to import all objects in a module


def run_pytests_modules(*test_modules):
    tfunction, tsuccess, c = 0, 0, None
    t1 = time.time()
    for module in test_modules:
        functions = import_module_tests_functions(module)
        print("[INFO] ... Runing {0} tests : [{1} functions]".format(module, len(functions)))
        if not functions:
            print("       ====> Skipped [NO FUNCTIONS]")
            print("")
            continue
        k1 = time.time()
        for func in functions:
            c = _test_function(func)
            tfunction += 1
            if c:
                tsuccess += 1
        k2 = time.time()
        print("        ====> Module tests total run time : {0} ms".format(k2 - k1))
        print("        ====> end module test")
        print("")
    t2 = time.time()
    sr = tsuccess/tfunction * 100
    print('[INFO] ... --- end test ---')
    print('       ====> Total runtime : {0} ms'.format(t2 - t1))
    print('       ====> Success rate : {0}  [ {1}/{2} ]'.format(sr, tsuccess, tfunction))
    # proc test error (for CI)
    if sr < 100:
        raise TestFail()


def run_all_tests():
    run_pytests_modules(*test_modules)


if __name__ == "__main__":
    run_all_tests()
