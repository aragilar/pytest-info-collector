from setuptools import setup
import versioneer

setup(
    name="pytest-info-collector",
    version=versioneer.get_version(),
    packages = ['pytest_info_collector'],
    install_requires = ["pytest"],
    author = "James Tocknell",
    author_email = "aragilar@gmail.com",
    description = "Solver thing",
    #license = "BSD",
    #keywords = "wheel",
    url = "http://pytest_info_collector.rtfd.io",
    entry_points = {
        'pytest11': [
            'name_of_plugin = pytest_info_collector',
        ]
    },
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    cmdclass=versioneer.get_cmdclass(),
)
