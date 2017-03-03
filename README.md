[![Documentation Status](https://readthedocs.org/projects/pytest-info-collector/badge/?version=latest)](http://pytest-info-collector.readthedocs.org/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/aragilar/pytest-info-collector.svg?branch=master)](https://travis-ci.org/aragilar/pytest-info-collector)
[![Coverage Status](https://codecov.io/github/aragilar/pytest-info-collector/coverage.svg?branch=master)](https://codecov.io/github/aragilar/pytest-info-collector?branch=master)
[![Version](https://img.shields.io/pypi/v/pytest-info-collector.svg)](https://pypi.python.org/pypi/pytest-info-collector/)
[![License](https://img.shields.io/pypi/l/pytest-info-collector.svg)](https://pypi.python.org/pypi/pytest-info-collector/)
[![Wheel](https://img.shields.io/pypi/wheel/pytest-info-collector.svg)](https://pypi.python.org/pypi/pytest-info-collector/)
[![Format](https://img.shields.io/pypi/format/pytest-info-collector.svg)](https://pypi.python.org/pypi/pytest-info-collector/)
[![Supported versions](https://img.shields.io/pypi/pyversions/pytest-info-collector.svg)](https://pypi.python.org/pypi/pytest-info-collector/)
[![Supported implemntations](https://img.shields.io/pypi/implementation/pytest-info-collector.svg)](https://pypi.python.org/pypi/pytest-info-collector/)
[![PyPI](https://img.shields.io/pypi/status/pytest-info-collector.svg)](https://pypi.python.org/pypi/pytest-info-collector/)

`pytest_info_collector` is a plugin for pytest providing a fixture for collecting
information from tests and displaying it, independent of the test status.

A simple example of this is:
```python

    def test_single(test_info):
        test_info("A simple test")
```
which would display "A simple test" at the end of the tests. Further
documentation can be found at [https://pytest-info-collector.readthedocs.io](https://pytest-info-collector.readthedocs.io).

Bug reports and suggestions should be filed at
[https://github.com/aragilar/pytest-info-collector/issues](https://github.com/aragilar/pytest-info-collector/issues).
