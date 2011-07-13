#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'mpttadmin',
    version = '0.3.2',
    author = 'Mikhail Sakhno',
    author_email = 'pawn13@gmail.com',
    description = """jstree admin for mptt models""",
    license = "BSD",
    keywords = "django admin",
    platforms = "POSIX",
    url = 'http://code.tabed.org/mptt_admin',
    install_requires=[],
    packages=[],#find_packages(),
    package_data = { 'media': [
        'js/*.js',
        'js/lib/*.js',
        'js/lib/plugins/*.js',
        'js/lib/themes/*/*',
    ]},
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
