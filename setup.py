# setup.py
from setuptools import setup, find_packages

setup(
    name="diag_tester",
    version="0.1.0",
    packages=find_packages(include=["diag_tester*"]),
    package_dir={"": "."},
    install_requires=[
        "pytest>=7.4.0",
        "allure-pytest>=2.13.2",
    ],
    python_requires=">=3.8",
)