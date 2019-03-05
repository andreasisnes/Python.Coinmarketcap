# -*- coding: utf-8 -*-

from os.path import join, dirname
from setuptools import setup


def read(fname):
    with open(join(dirname(__file__), fname), encoding="utf-8") as f:
        return f.read()


setup(
    # Package
    name="PyCoinMarketCap",
    version="0.2",
    packages=["coinmarketcap"],
    url="https://github.com/ani071/coinmarketcap",
    keywords=["CoinMarketCap", "API"],
    install_requires=["requests_cache", "requests", "ratelimit"],
    # Contact
    author="Andreas Isnes Nilsen",
    author_email="andnil94@gmail.com",
    # Description
    description="Module for fethcing data from CoinMarketCap's v1 API",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
)
