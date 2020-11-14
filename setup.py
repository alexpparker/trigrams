from setuptools import setup

dependencies = ["pytest", "pytest-cov"]


setup(
    name="trigrams_pkg",
    description="A text generator using trigrams algorithm",
    package_dir={"": "src"},
    install_requires=dependencies
)
