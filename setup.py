############################################################################
# This module is a part of the Polyrot numerical package.  
#
# Copyright (C) 2023 Janosz Dewberry
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License as published by the 
# Free Software Foundation, version 3.
#
# Polyrot is distributed in the hope that it will be useful, but WITHOUT ANY 
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more 
# details.
#
# You should have received a copy of the GNU General Public License along 
# with this program. If not, see http://www.gnu.org/licenses/.
############################################################################

from setuptools import setup

setup(
    name="polyrot",
    version="0.0.1",
    description="A small package for computing polytropic models of rapidly rotating planets and stars",
    author="Janosz Dewberry",
    author_email="jdewberry@cita.utoronto.ca",
    license="GPL-3.0-only",
    url="https://github.com/dewberryjanosz/polyrot",
    packages=['polyrot'],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
