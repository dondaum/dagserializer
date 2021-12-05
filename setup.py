# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# The text of the README file
with open("README.md") as f:
    readme = f.read()

with open("requirements.txt") as f:
    pip_packages = f.read()

DESC = """
This library serialize a dbt DAG to a static
Airflow DAG.
"""

# This call to setup() does all the work
setup(
    name="dagserializer",
    version="0.0.1",
    description=DESC,
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Sebastian Daum",
    author_email="S40844@eon.com",
    url="",  # noqa: E501
    test_suite="tests",
    classifiers=[
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',

        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={'dagserializer': ['py.typed']},
    entry_points={
        "console_scripts": [
            "dagserializer = dagserializer.__main__"
        ]
    },
    install_requires=[pip_packages.split('\n')],
    zip_safe=False,
)