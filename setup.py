from setuptools import setup

from hello import __version__

setup(
    name='hello',
    version=__version__,

    url='https://github.com/ericnost/hello',
    author='Eric Nost',
    author_email='enost@uoguelph.ca',

    py_modules=['hello'],
)