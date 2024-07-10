from setuptools import setup, find_packages
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    next(f)  # Ignoring first line
    long_description = f.read()


## Required files
__version__ = "0.0.12"
REPO_NAME = "dstemplatest-pypi"
PKG_NAME = "dstemplatest"  # package will be visible with this name in PyPI
AUTHOR_USER_NAME = "ravi46931"  # GitHub user name
AUTHOR_EMAIL = "ravikumar46931@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for creating project structure.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    # Install requires may be added at here
    install_requires=[
        "pandas",
        "numpy"  
    ],
)