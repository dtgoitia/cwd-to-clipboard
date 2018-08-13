# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from setuptools import find_packages, setup

setup(
    name='cwd-to-clipboard',
    version='0.0.1',
    description='Current Working Directory to Clipboard',
    author='David Torralba Goitia',
    author_email='david.torralba.goitia@gmail.com',
    packages=find_packages(exclude=['tests']),
    license='MIT',
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
    keywords=['cli', 'tool'],
    install_requires=['pyperclip'],
    entry_points={
        'console_scripts': [
            'cwd-to-clipboard=cwd_to_clipboard.__main__:main'
        ]
    }
)
