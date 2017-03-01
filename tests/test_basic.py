pytest_plugins = "pytester"  # to get testdir fixture

def test_single(testdir):
    testdir.makepyfile("""
        def test_single(test_info):
            test_info("A simple test")
    """)
    result = testdir.runpytest()
    result.stdout.fnmatch_lines("""
        *test_single: A simple test*
    """)
