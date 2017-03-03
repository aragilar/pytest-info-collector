from setuptools import setup
import versioneer

DESCRIPTION_FILES = ["pypi-intro.rst"]

long_description = []
import codecs
for filename in DESCRIPTION_FILES:
    with codecs.open(filename, 'r', 'utf-8') as f:
        long_description.append(f.read())
long_description = "\n".join(long_description)

setup(
    name="pytest-info-collector",
    version=versioneer.get_version(),
    packages = ['pytest_info_collector'],
    install_requires = ["pytest"],
    author = "James Tocknell",
    author_email = "aragilar@gmail.com",
    description = "pytest plugin to collect information from tests",
    long_description = long_description,
    license = "3-clause BSD",
    keywords = "pytest testing",
    url = "https://pytest-info-collector.readthedocs.io",
    entry_points = {
        'pytest11': [
            'name_of_plugin = pytest_info_collector',
        ]
    },
    classifiers=[
        'Framework :: Pytest',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
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
