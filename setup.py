from setuptools import setup, find_packages

from hello import __version__

setup(
    name='hello',
    version=__version__,

    url='https://github.com/ericnost/hello',
    author='Eric Nost',
    author_email='enost@uoguelph.ca',

    packages=find_packages()
)