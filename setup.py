from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.1dev2"

setup(
    name="hivetoolkit",
    version=__version__,
    url="https://github.com/slashformotion/hivetools",
    license="MIT",
    author="slashformotion",
    author_email="slashformotion@protonmail.com",
    description="A set of tools to work with the Hive (or Steem) blockchain",
    packages=find_packages(exclude=("tests",)),
    install_requires=['beem'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Office/Business :: Financial",
    ],
)
