from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = '0.0.1'

setup(
    name='hivetoolkit',
    version=__version__,
    url='https://github.com/slashformotion/hivetools',
    license='MIT',
    author='Gigi Sayfan',
    author_email='slashformotion@protonmail.com',
    description='A set of tools to work with the Hive (or Steem) blockchain',
    packages=['hivetoolkit'],
    long_description=long_description,
    long_description_content_type='text/markdown')