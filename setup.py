# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

requires = ['click', 'cairocffi', 'CairoSVG', 'cffi', 'cssselect', 'docopt', 'html5lib', 'Jinja2', 'lxml',
            'Markdown', 'MarkupSafe', 'pycparser', 'Pyphen', 'PyYAML', 'six', 'tinycss', 'wkhtmltopdf', 'pdfkit',
            'xhtml2pdf', 'yaml']

setup(
    name="Kevin Ciarniello's Resume",
    author="Kevin Ciarniello",
    author_email="kciarnie@gmail.com",
    description="A resume of what I have done",
    long_description="\n\n".join([open("README.md").read()]),
    license='MIT',
    url="https://bitbucket.org/kciarnie/resume.git",
    packages=find_packages(),
    install_requires=requires,
    entry_points={'console_scripts': [
        'resume = build:main'
    ]},
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython']
)
