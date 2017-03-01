pytest_plugins = "pytester"  # to get testdir fixture


def test_single(testdir):
    testdir.makepyfile("""
        def test_single(test_info):
            test_info("A simple test")
    """)
    result = testdir.runpytest()
    result.stdout.fnmatch_lines("""
        *test_single: A simple test
    """)


def test_multiple(testdir):
    testdir.makepyfile("""
        def test_multiple(test_info):
            test_info("First one")
            test_info("Second one")
    """)
    result = testdir.runpytest()
    result.stdout.fnmatch_lines("""
        test_multiple: First one
        test_multiple: Second one
    """)

def test_many_tests(testdir):
    testdir.makepyfile("""
        def test_many_tests1(test_info):
            test_info("First one")
            test_info("Second one")

        def test_many_tests2(test_info):
            test_info("Second test one")
            test_info("Second test two")
    """)
    result = testdir.runpytest()
    result.stdout.fnmatch_lines("""
        test_many_tests1: First one
        test_many_tests1: Second one
    """)
    result.stdout.fnmatch_lines("""
        test_many_tests2: Second test one
        test_many_tests2: Second test two
    """)

