"""
A simple pytest plugin which collects test information and prints it at the end
of the tests
"""
from collections import defaultdict
import pytest

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


class InfoCollector:
    """
    Main driver of test information collection
    """
    def __init__(self):
        self._info = defaultdict(list)

    def pytest_terminal_summary(self, terminalreporter, exitstatus):
        """
        Hook for printing test info at the end of the run
        """
        # pylint: disable=unused-argument
        terminalreporter.section("Test Information")
        for test, info in self._info.items():
            for datum in info:
                terminalreporter.write("{}: {}\n".format(test, datum))

    @pytest.fixture
    def test_info(self, request):
        """
        Fixture to collect test information
        """
        def add_info(info):
            """
            Adds information about test
            """
            self._info[get_test_name(request)].append(info)
        return add_info


def get_test_name(request):
    """
    Get the name of test from pytest
    """
    return request.node.name


def pytest_configure(config):
    """Add plugin to pytest"""
    config.pluginmanager.register(InfoCollector(), "info_collector")
