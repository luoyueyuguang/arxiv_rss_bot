#!/usr/bin/env python3
"""
Setup script for arXiv Bot
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith("#")
    ]

setup(
    name="arxiv-rss-bot",
    version="1.0.0",
    author="maydomine",
    description="An automated bot that fetches papers from arXiv RSS feeds and updates README.md",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maydomine/arxiv_rss_bot",
    license="MIT",
    packages=find_packages(exclude=("tests", "tests.*")),
    py_modules=["arxiv_bot", "base_conference_bot", "run_all_bots"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "arxiv-bot=arxiv_bot:main",
        ],
    },
)
