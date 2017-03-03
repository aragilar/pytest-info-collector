`pytest_info_collector` is a plugin for pytest providing a fixture for collecting
information from tests and displaying it, independent of the test status.

A simple example of this is:

::

    def test_single(test_info):
        test_info("A simple test")

which would display "A simple test" at the end of the tests. Further
documentation can be found at `<https://pytest-info-collector.readthedocs.io>`_.

Bug reports and suggestions should be filed at
`<https://github.com/aragilar/pytest-info-collector/issues>`_.


|Documentation Status| |Build Status| |Coverage Status|

.. |Documentation Status| image:: https://readthedocs.org/projects/pytest-info-collector/badge/?version=latest
   :target: http://pytest-info-collector.readthedocs.org/en/latest/?badge=latest
.. |Build Status| image:: https://travis-ci.org/aragilar/pytest-info-collector.svg?branch=master
   :target: https://travis-ci.org/aragilar/pytest-info-collector
.. |Coverage Status| image:: https://codecov.io/github/aragilar/pytest-info-collector/coverage.svg?branch=master
   :target: https://codecov.io/github/aragilar/pytest-info-collector?branch=master
